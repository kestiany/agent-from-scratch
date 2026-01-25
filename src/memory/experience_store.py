from typing import List, Dict
from datetime import datetime
from collections import defaultdict

from schema.experience import TaskExperience


class ExperienceStore:
    """
    Experience Store = 系统的“事实记忆层”
    只存客观结果，不存推理、不存策略、不存判断
    """

    def __init__(self):
        # in-memory store（Week 7 形态）
        self._experiences: Dict[str, TaskExperience] = {}
        self._index_by_domain: Dict[str, List[str]] = defaultdict(list)
        self._index_by_task_type: Dict[str, List[str]] = defaultdict(list)

    # ========== 写入 ==========

    def add(self, exp: TaskExperience):
        """
        写入一次完整任务经验
        """
        self._experiences[exp.task_id] = exp

        # 建立轻索引（为 Pattern / Advisory 服务）
        for sig in exp.plan_outline:
            if sig.domain:
                self._index_by_domain[sig.domain].append(exp.task_id)
            if sig.task_type:
                self._index_by_task_type[sig.task_type].append(exp.task_id)

    # ========== 读取 ==========

    def get(self, task_id: str) -> TaskExperience | None:
        return self._experiences.get(task_id)

    def all(self) -> List[TaskExperience]:
        return list(self._experiences.values())

    # ========== 查询接口（给 Pattern 用） ==========

    def query(
        self,
        domain: str | None = None,
        task_type: str | None = None,
        status: str | None = None,
    ) -> List[TaskExperience]:
        """
        Week 7 版查询能力：
        - domain
        - task_type
        - status（success / fail / partial）
        """

        candidates: set[str] = set(self._experiences.keys())

        if domain:
            candidates &= set(self._index_by_domain.get(domain, []))

        if task_type:
            candidates &= set(self._index_by_task_type.get(task_type, []))

        result = []
        for tid in candidates:
            exp = self._experiences[tid]
            if status:
                if exp.result.status != status:
                    continue
            result.append(exp)

        return result

    # ========== 统计接口（给 Pattern / Experiment 用） ==========

    def stats(self) -> dict:
        """
        纯统计信息，不带业务逻辑
        """
        total = len(self._experiences)
        by_status = defaultdict(int)
        by_domain = defaultdict(int)

        for exp in self._experiences.values():
            by_status[exp.result.status] += 1
            for sig in exp.plan_outline:
                if sig.domain:
                    by_domain[sig.domain] += 1

        return {
            "total": total,
            "by_status": dict(by_status),
            "by_domain": dict(by_domain),
        }

    # ========== 管理接口 ==========

    def clear(self):
        """
        用于实验 / 测试
        """
        self._experiences.clear()
        self._index_by_domain.clear()
        self._index_by_task_type.clear()

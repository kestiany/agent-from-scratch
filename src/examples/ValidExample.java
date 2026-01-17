package com.example.demo;

public class ValidExample {

    private UserRepository userRepository;

    public ValidExample(UserRepository userRepository) {
        this.userRepository = userRepository;
    }

    public String process(Long userId) {
        User user = userRepository.findById(userId);

        // 潜在空指针风险：user 可能为 null
        return user.getName().toUpperCase();
    }

}

/**
 * 模拟仓储接口
 */
interface UserRepository {
    User findById(Long id);
}

/**
 * 简单的领域对象
 */
class User {
    private String name;

    public User(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }
}

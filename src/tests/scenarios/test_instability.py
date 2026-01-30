from agent.kernel import AgentKernel


def test_no_risk_found_should_fail():
    kernel = AgentKernel()
    result = kernel.run("Analyze empty file")

    assert result["status"] in ["terminated", "insufficient_info"]
    assert result["confidence"] < 0.5

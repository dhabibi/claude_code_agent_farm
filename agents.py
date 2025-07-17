# agents.py

from abc import ABC, abstractmethod

class BaseAgent(ABC):
    """
    Abstract base class for all agents.
    Defines standardized interface for agent detection and control.
    """

    @abstractmethod
    def detect(self, context):
        """
        Detect agent status or capabilities.
        Args:
            context: Arbitrary context or configuration.
        Returns:
            Detection result (implementation-specific).
        """
        pass

    @abstractmethod
    def control(self, command, **kwargs):
        """
        Control the agent with a command.
        Args:
            command: Command string or object.
            kwargs: Additional parameters.
        Returns:
            Control result (implementation-specific).
        """
        pass

class ClaudeCodeAgent(BaseAgent):
    """
    Concrete agent implementation for Claude Code.
    """

    def detect(self, context):
        # Example detection logic for Claude Code agent
        return {"agent": "ClaudeCode", "status": "active", "context": context}

    def control(self, command, **kwargs):
        # Example control logic for Claude Code agent
        return {"agent": "ClaudeCode", "command": command, "result": "success", "params": kwargs}

class OpenCodeAgent(BaseAgent):
    """
    Concrete agent implementation for Open Code.
    """

    def detect(self, context):
        # Example detection logic for Open Code agent
        return {"agent": "OpenCode", "status": "active", "context": context}

    def control(self, command, **kwargs):
        # Example control logic for Open Code agent
        return {"agent": "OpenCode", "command": command, "result": "success", "params": kwargs}

class AgentFactory:
    """
    Factory for instantiating agents based on configuration.
    Extensible for future agent types.
    """

    @staticmethod
    def create_agent(agent_type, **kwargs):
        """
        Instantiate the correct agent type.
        Args:
            agent_type: String identifier for agent type.
            kwargs: Additional parameters for agent initialization.
        Returns:
            Instance of BaseAgent subclass.
        Raises:
            ValueError if agent_type is unknown.
        """
        if agent_type == "claude_code":
            return ClaudeCodeAgent(**kwargs)
        elif agent_type == "open_code":
            return OpenCodeAgent(**kwargs)
        else:
            raise ValueError(f"Unknown agent type: {agent_type}")
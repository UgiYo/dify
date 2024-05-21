from typing import Any

from core.tools.entities.values import ToolLabelEnum
from core.tools.errors import ToolProviderCredentialValidationError
from core.tools.provider.builtin.wolframalpha.tools.wolframalpha import WolframAlphaTool
from core.tools.provider.builtin_tool_provider import BuiltinToolProviderController


class GoogleProvider(BuiltinToolProviderController):
    def _validate_credentials(self, credentials: dict[str, Any]) -> None:
        try:
            WolframAlphaTool().fork_tool_runtime(
                meta={
                    "credentials": credentials,
                }
            ).invoke(
                user_id='',
                tool_parameters={
                    "query": "1+2+....+111",
                },
            )
        except Exception as e:
            raise ToolProviderCredentialValidationError(str(e))
    
    def _get_tool_labels(self) -> list[ToolLabelEnum]:
        return [
            ToolLabelEnum.PRODUCTIVITY, ToolLabelEnum.UTILITIES
        ]
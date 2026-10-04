# Open Quantum ChatGPT MCP bridge

A minimal Streamable HTTP MCP endpoint for ChatGPT backed by the official `openquantum-sdk`.

## Security

- Open Quantum SDK credentials are environment variables only. Never commit them.
- Real QPU submission is disabled unless `OPENQUANTUM_ENABLE_SUBMIT=true`.
- Even when enabled, only the exact `OPENQUANTUM_ALLOWED_PREPARATION_ID` can be submitted.
- Non-zero quotes require `confirm_spend=true`.
- `OPENQUANTUM_MCP_MAX_CREDITS` is a server-side hard cap (default: 2).
- `OPENQUANTUM_MCP_MAX_SHOTS` caps shot count (default: 128).

## Workflow

1. `get_backend`
2. `prepare_job` (validation + quote; no QPU spend)
3. Review `quote_summary`
4. Server operator temporarily allowlists the preparation ID
5. `submit_prepared_job`
6. Disable submission again
7. `get_job`, `get_job_results`, and optionally `get_job_calibration`

The MCP endpoint is `/mcp`.

import { request } from "./apiClient.ts";
import type { HealthResponse, ServiceStatus } from "../types/health.ts";

export async function checkBackendHealth(): Promise<ServiceStatus> {
  const startTime = performance.now();
  try {
    const data = await request<HealthResponse>("/health");
    const latencyMs = Math.round(performance.now() - startTime);
    return {
      connected: data.status === "ok",
      data,
      latencyMs,
    };
  } catch (err: unknown) {
    const message = err instanceof Error ? err.message : "Failed to connect to backend";
    return {
      connected: false,
      error: message,
    };
  }
}

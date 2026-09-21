export interface HealthResponse {
  status: string;
  app_name: string;
  version: string;
  environment: string;
}

export interface ServiceStatus {
  connected: boolean;
  data?: HealthResponse;
  error?: string;
  latencyMs?: number;
}

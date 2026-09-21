import React from "react";
import { Bot, RefreshCw } from "lucide-react";
import type { ServiceStatus } from "../types/health.ts";

interface HeaderProps {
  status: ServiceStatus;
  isChecking: boolean;
  onRefresh: () => void;
}

export const Header: React.FC<HeaderProps> = ({ status, isChecking, onRefresh }) => {
  return (
    <header className="header-container" id="app-header">
      <div className="brand-section">
        <div className="brand-logo-icon" aria-hidden="true">
          <Bot size={24} />
        </div>
        <div className="brand-text">
          <h1 id="app-title">Enterprise Knowledge & Task Assistant</h1>
          <p>ASK • FIND • ACT Corporate Intelligence Platform</p>
        </div>
      </div>

      <div style={{ display: "flex", alignItems: "center", gap: "1rem" }}>
        <div
          id="backend-status-indicator"
          className={`status-badge ${
            isChecking
              ? "checking"
              : status.connected
              ? "connected"
              : "disconnected"
          }`}
        >
          <span className="status-dot" aria-hidden="true" />
          <span>
            {isChecking
              ? "Checking Backend..."
              : status.connected
              ? `Backend Connected (${status.latencyMs ?? 0}ms)`
              : "Backend Offline"}
          </span>
        </div>

        <button
          id="refresh-health-btn"
          className="retry-btn"
          onClick={onRefresh}
          disabled={isChecking}
          title="Refresh connection status"
        >
          <RefreshCw size={14} className={isChecking ? "spin-animation" : ""} />
          <span>Check Status</span>
        </button>
      </div>
    </header>
  );
};

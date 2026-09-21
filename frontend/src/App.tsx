import React, { useEffect, useState, useCallback } from "react";
import { Header } from "./components/Header.tsx";
import { CapabilityCard } from "./components/CapabilityCard.tsx";
import { checkBackendHealth } from "./services/healthService.ts";
import type { ServiceStatus } from "./types/health.ts";
import { ShieldCheck, Database, Layers } from "lucide-react";

export const App: React.FC = () => {
  const [status, setStatus] = useState<ServiceStatus>({ connected: false });
  const [isChecking, setIsChecking] = useState<boolean>(true);

  const fetchHealth = useCallback(async () => {
    setIsChecking(true);
    const result = await checkBackendHealth();
    setStatus(result);
    setIsChecking(false);
  }, []);

  useEffect(() => {
    fetchHealth();
    // Poll health status every 30 seconds
    const interval = setInterval(fetchHealth, 30000);
    return () => clearInterval(interval);
  }, [fetchHealth]);

  return (
    <div className="app-wrapper">
      <Header status={status} isChecking={isChecking} onRefresh={fetchHealth} />

      <main className="main-container">
        {/* Hero Section */}
        <section className="hero-section">
          <div className="hero-pill">
            <Layers size={14} />
            <span>Enterprise Architecture Initialized</span>
          </div>
          <h1 className="hero-title">
            Corporate Knowledge &amp; Task <span className="gradient-text">Assistant</span>
          </h1>
          <p className="hero-description">
            Interact with corporate knowledge and enterprise business systems securely
            using natural language. Grounded in corporate documents, live APIs, and Microsoft Azure AI.
          </p>
        </section>

        {/* Real-time System Connectivity Card */}
        <section className="system-status-box" id="system-status-panel">
          <div className="system-meta-item">
            <span className="meta-label">Backend Service</span>
            <span className="meta-value" id="meta-app-name">
              {status.data?.app_name || "Enterprise Knowledge Backend"}
            </span>
          </div>
          <div className="system-meta-item">
            <span className="meta-label">Version</span>
            <span className="meta-value" id="meta-version">
              {status.data?.version || "v0.1.0"}
            </span>
          </div>
          <div className="system-meta-item">
            <span className="meta-label">Active Environment</span>
            <span className="meta-value" id="meta-environment">
              {status.data?.environment || "development"}
            </span>
          </div>
          <div className="system-meta-item">
            <span className="meta-label">Endpoint Probe</span>
            <span
              className="meta-value"
              id="meta-probe"
              style={{ color: status.connected ? "var(--accent-emerald)" : "var(--accent-rose)" }}
            >
              {status.connected
                ? `HTTP 200 OK (${status.latencyMs ?? 0}ms)`
                : status.error || "Connecting..."}
            </span>
          </div>
          <div className="system-meta-item">
            <span className="meta-label">Security &amp; Auth</span>
            <span
              className="meta-value"
              style={{ display: "flex", alignItems: "center", gap: "0.35rem", color: "var(--accent-cyan)" }}
            >
              <ShieldCheck size={16} /> Entra ID Ready (Mock Dev)
            </span>
          </div>
        </section>

        {/* 3 Pillars: ASK / FIND / ACT */}
        <section className="capabilities-grid" id="capabilities-section">
          <CapabilityCard
            type="ask"
            badge="01 • Corporate Knowledge"
            title="ASK"
            description="Answer corporate policy, handbook, SOP, and procedure questions grounded strictly in organizational documents."
            techStack="Azure AI Search • Azure Blob • RAG Pipeline"
            examples={[
              "What is the work-from-home policy?",
              "Can I claim hotel expenses during business travel?",
              "Does the leave policy apply to interns?",
            ]}
          />

          <CapabilityCard
            type="find"
            badge="02 • Personalized Information"
            title="FIND"
            description="Retrieve live, authenticated employee records, balances, ticket statuses, and project details from internal systems."
            techStack="Internal APIs • HR & ITSM Systems • Entra RBAC"
            examples={[
              "How many leaves do I have remaining?",
              "What is the status of my expense claim?",
              "Show me my open IT tickets",
            ]}
          />

          <CapabilityCard
            type="act"
            badge="03 • Business Tasks"
            title="ACT"
            description="Execute authorized business workflows with built-in human-in-the-loop review and transactional confirmation."
            techStack="LangChain Tool Calling • ITSM & HR Action APIs"
            examples={[
              "Create an IT ticket: laptop won't connect to Wi-Fi",
              "Submit leave request for Oct 12-14",
              "Request a replacement developer laptop",
            ]}
          />
        </section>

        {/* Architecture Note */}
        <section
          style={{
            background: "rgba(17, 24, 39, 0.4)",
            border: "1px solid var(--border-color)",
            borderRadius: "var(--radius-lg)",
            padding: "1.75rem",
            display: "flex",
            alignItems: "flex-start",
            gap: "1.25rem",
          }}
        >
          <div
            style={{
              background: "rgba(59, 130, 246, 0.1)",
              padding: "0.75rem",
              borderRadius: "var(--radius-md)",
              color: "var(--accent-blue)",
            }}
          >
            <Database size={24} />
          </div>
          <div>
            <h3 style={{ fontSize: "1.05rem", fontWeight: 600, marginBottom: "0.4rem" }}>
              Architectural Separation of Concerns
            </h3>
            <p style={{ fontSize: "0.88rem", color: "var(--text-secondary)", lineHeight: 1.6 }}>
              The project enforces strict modular boundaries: React (TypeScript) for client presentation,
              FastAPI for HTTP route handling and security context, LangChain for intent routing and tool
              orchestration, and Azure AI Search for grounded retrieval. Sensitive actions require affirmative user confirmation.
            </p>
          </div>
        </section>
      </main>

      {/* Footer */}
      <footer className="footer-container">
        <p>Enterprise Knowledge &amp; Task Assistant • Initial Project Skeleton • AGENTS.md Compliant</p>
      </footer>
    </div>
  );
};

export default App;

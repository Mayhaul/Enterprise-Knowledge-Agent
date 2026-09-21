import React from "react";
import { BookOpen, Search, Zap } from "lucide-react";

interface CapabilityProps {
  type: "ask" | "find" | "act";
  badge: string;
  title: string;
  description: string;
  examples: string[];
  techStack: string;
}

export const CapabilityCard: React.FC<CapabilityProps> = ({
  type,
  badge,
  title,
  description,
  examples,
  techStack,
}) => {
  const getIcon = () => {
    switch (type) {
      case "ask":
        return <BookOpen size={24} />;
      case "find":
        return <Search size={24} />;
      case "act":
        return <Zap size={24} />;
    }
  };

  return (
    <div className="capability-card" id={`card-capability-${type}`}>
      <div className={`card-icon-container ${type}`} aria-hidden="true">
        {getIcon()}
      </div>
      <div className="card-badge">{badge}</div>
      <h2 className="card-title">{title}</h2>
      <p className="card-desc">{description}</p>

      <div style={{ marginBottom: "1rem" }}>
        <div className="card-examples-title">Integration Layer</div>
        <span
          style={{
            fontFamily: "var(--font-mono)",
            fontSize: "0.78rem",
            color: "var(--accent-cyan)",
          }}
        >
          {techStack}
        </span>
      </div>

      <div className="card-examples">
        <div className="card-examples-title">Example Prompts</div>
        {examples.map((example, idx) => (
          <span key={idx} className="example-tag">
            "{example}"
          </span>
        ))}
      </div>
    </div>
  );
};

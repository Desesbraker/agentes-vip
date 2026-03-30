import handler from "@tanstack/react-start/server-entry";

// Export Workflow classes as named exports
export { SiteAuditWorkflow } from "./server/workflows/SiteAuditWorkflow";

export default {
  fetch: handler.fetch,
};

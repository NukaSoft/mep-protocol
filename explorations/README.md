# MEP Explorations

Dead ends, roads taken and rejected, ideas in flight.  This is the sketchbook.

Every serious protocol gets built through elimination.  The final spec looks clean because we killed a lot of bad ideas on the way to it.  This directory is the proof of work.  It is also useful to anyone building a fork | if you are thinking "what about X," there is a good chance we tried it.

## Format

Each file is one exploration.  Frontmatter declares status.  The body explains what we tried, what we found, and why we decided what we decided.

```yaml
---
status: rejected | tried | active | shelved
date: YYYY-MM-DD
proposed_by: Pierre
outcome: one line
---
```

## Index

| File | What We Tried | Status |
|------|---------------|--------|
| [s3-redshift-hosted-relay.md](s3-redshift-hosted-relay.md) | S3 + Redshift as a managed baton store with a public query surface | Rejected |
| [bluesky-atproto-transport.md](bluesky-atproto-transport.md) | Bluesky AT Protocol as real-time inter-agent message bus | Shelved |
| [hello-protocol.md](hello-protocol.md) | Formalizing the `hello` message as a startup event in the MEP lifecycle | Active |
| [google-drive-shared-surface.md](google-drive-shared-surface.md) | Google Drive as the cross-ecosystem shared handoff surface | Active (v2.1) |
| [smb-umb-file-locking.md](smb-umb-file-locking.md) | Shared file systems (SMB/UMB) as transport layer | Rejected |

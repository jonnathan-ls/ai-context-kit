# Changelog Template (Keep a Changelog)

Follow the [Keep a Changelog](https://keepachangelog.com) format.

## Template

```markdown
# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased]

### Added
- New feature description

## [1.2.0] - 2026-03-15

### Added
- User profile avatars

### Changed
- Improved search response time by 40%

### Fixed
- Resolved race condition in payment processing

### Deprecated
- Legacy `/v1/auth` endpoints (use `/v2/auth`)

## [1.0.0] - 2026-01-01

### Added
- Initial release
```

## Section Types

| Section | What Goes Here |
|---------|---------------|
| **Added** | New features |
| **Changed** | Changes to existing behavior |
| **Deprecated** | Features that will be removed |
| **Removed** | Features removed in this version |
| **Fixed** | Bug fixes |
| **Security** | Security patches |

## Rules

- Most recent version at the top.
- Always maintain an `[Unreleased]` section for in-progress changes.
- Use ISO dates (`YYYY-MM-DD`).
- Write from the user's perspective — what changed for them, not what you did in code.
- One item per bullet. Be specific enough to be useful ("Improved search response time by 40%"), not vague ("Performance improvements").

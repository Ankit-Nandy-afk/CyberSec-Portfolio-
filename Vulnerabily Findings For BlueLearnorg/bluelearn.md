# Bluelearn Contributions

Open-source contributions to [bluelearn-org/bluelearn](https://github.com/bluelearn-org/bluelearn), a non-profit learning platform built around a prerequisite graph of concepts.

[![Commits](https://img.shields.io/badge/Full%20Commit%20History-View-2ea44f?style=for-the-badge&logo=github)](https://github.com/bluelearn-org/bluelearn/commits?author=Ankit-Nandy-afk)

**Role:** Director & Security / Privacy Lead
**Active period:** Aug 9 – Sep 23, 2026
**Scope:** Full-stack work across the editor, database schema, API routes, tests, and UI polish. Many commits are GPG/SSH-signed (Verified).

---

## Highlights

| Area | What I did |
|---|---|
| Editor | Added a source mode and fixed fullscreen, toolbar, and blur bugs |
| Database / API | Renamed core tables and kept the SQL functions, routes, and tests consistent |
| Data integrity | Made the UI handle deleted accounts safely |
| UX | Fixed mobile layout issues and added a mascot to the 404 page |
| Code quality | Prettier formatting and repo cleanup |

---

## Editor

- **Source mode:** added a source view to the editor, with follow-up formatting and cleanup
  - [added source mode](https://github.com/bluelearn-org/bluelearn/commit/b769f4d6f16afd1bab91483e1f2ff86e750c7c41)
  - [source mode](https://github.com/bluelearn-org/bluelearn/commit/69cac6cb663186f1a2cc3af498333fecc81ea4f8)
  - [Delete editor-source-mode.css](https://github.com/bluelearn-org/bluelearn/commit/3ccead0f9345d804cfa0e5d8c24af43b16e1ccf5)
  - [remove untracked supabase snippets and format editor code](https://github.com/bluelearn-org/bluelearn/commit/14f30f94fcef6a0fe72e75b4cfd21071054227e4)
- **Fullscreen and toolbar fixes:**
  - [raise tooltip z-index to prevent overlap in fullscreen mode](https://github.com/bluelearn-org/bluelearn/commit/f172de38901ccdd3f9461d49661a7e4662c9f06d)
  - [fix blur bleed](https://github.com/bluelearn-org/bluelearn/commit/c62bbfc268047c370bfb82c1f46e88d7e6a78f79)
  - [isolate toolbar](https://github.com/bluelearn-org/bluelearn/commit/8564a29b57d76a1b84e2cd9350f992de0ff3a328)
  - [isolate toolbar (follow-up)](https://github.com/bluelearn-org/bluelearn/commit/db3bfe28436906077a0d44c1a71f398265a4c656)
  - [fix blur](https://github.com/bluelearn-org/bluelearn/commit/421d94823b9c3be3972e3ec80d3399cabc96524e)
- **Math block input:** disallowed the space key inside math blocks ([merge into main](https://github.com/bluelearn-org/bluelearn/commit/1c3e48e2694ec5f204a04bdcab60204489be8832))

## Database and API

Renamed the `todo_prerequisites` / `todo_claims` tables to `requests` / `request_claims`, then followed the change through the SQL function, routes, and tests so nothing was left pointing at the old names.

- [Rename tables to requests / request_claims](https://github.com/bluelearn-org/bluelearn/commit/b10930b5cde586fd02a75bba3a91f3b94af58574)
- [Continue the rename](https://github.com/bluelearn-org/bluelearn/commit/c1fb1841ce1d54409e6afd4866a493f6745205fa)
- [Update `todo_has_open_claim` after the claim table rename](https://github.com/bluelearn-org/bluelearn/commit/e4718d0c27f74ae86551718ee2a9f8f347e85d51)
- [Rename remaining `todoPrereqs` reference in the edit route](https://github.com/bluelearn-org/bluelearn/commit/dd33ddd2391496162feb8fa0aa34d148ad2c26e4)
- [Add required `summary` field to the POST /todos test](https://github.com/bluelearn-org/bluelearn/commit/1d016ee8aeba37a401ba79641e4c048ad5533a88)

## Deleted-account handling

Made guide pages work correctly when an author deletes their account.

- [Fall back to `deleted_user` when the guide author is null in GuideCard](https://github.com/bluelearn-org/bluelearn/commit/939cb81d44323a7139dfdd9ad5ca2e29860a6498)
- [Mark guide author nullable to match the runtime shape](https://github.com/bluelearn-org/bluelearn/commit/18c2e500b9045e884450cc241ca38220ab6d82ae)
- [Resolve guide reader imports and heading id logic](https://github.com/bluelearn-org/bluelearn/commit/83c15341ad59f2f139384a0384f5050b3806fbbf)
- [Resolve parameter shadowing in themeProvider](https://github.com/bluelearn-org/bluelearn/commit/d8a4252962b78e1b4ce66b8906ef4e30fd8d1077)

## UI and UX

- [Prevent the Next button from clipping off-screen on mobile](https://github.com/bluelearn-org/bluelearn/commit/2df7838d5412ed63e4d85f7c73a75e5bafeac6ae)
- [Fix selected color on review decision buttons](https://github.com/bluelearn-org/bluelearn/commit/14c07521c8af99b313d4c21ad6881f24ff8dde10)
- [Add Adam mascot to the 404 page](https://github.com/bluelearn-org/bluelearn/commit/91c00357b3e8ecacb702eb36e848cb6fd7d17920)
- [Switch to a plain img tag (Vite project, not Next)](https://github.com/bluelearn-org/bluelearn/commit/8f7cb288275fa2e6db0967c73531874915048b2e)
- [Use plain img with responsive sizing](https://github.com/bluelearn-org/bluelearn/commit/c1a14bcf703c7ddbab2445637fc0b140d4553b05)
- [Add greyscale](https://github.com/bluelearn-org/bluelearn/commit/702f39eb52046c25016f361560b8cd1a228a4e96)

## Code quality

- [Format files with Prettier](https://github.com/bluelearn-org/bluelearn/commit/2f8053cc91a54165c87436cf19f15846239bd0c7)
- [Format code with Prettier](https://github.com/bluelearn-org/bluelearn/commit/c5fe68cad29fc48e3e75f134a28d73b45b571322)

---

## Security Work

My vulnerability research and audit notes for Bluelearn live in this repo: [Vulnerability Findings](./Vulnerabily%20Findings%20For%20BlueLearnorg).

[Back to portfolio](../README.md)

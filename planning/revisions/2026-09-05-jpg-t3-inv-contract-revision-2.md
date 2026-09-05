# JPG-T3-INV contract revision 2

Date: 2026-09-05

## Reason

The initial Issue #4 acceptance criterion required a Japanese-prefixed T3 image sequence that failed the helper's `page-NNN.jpg` input rule. The pinned T3 catalog and designated source instead contain the canonical sequence `page-001.jpg` through `page-344.jpg`, with matching hashes.

## Approved revision

T3 inventory execution must verify that the designated images already satisfy the helper input rule, copy them byte-for-byte under the same canonical names into ignored `project/T3/local-staging/`, and ingest that staging directory into the ignored canonical cache. The designated originals must not be renamed, overwritten or re-rendered. The inventory must preserve exact original-to-cache mapping and actual hashes, and stop on any unexpected noncanonical source file rather than inventing a rename.

## Unchanged contract

Issue #4 remains limited to T3 source inventory, page ownership, printed-page/exclusion mapping and boundary evidence. Its dependency declaration, 344-page scope, 18 planned batches, output schema, conversion stop condition and no-source-media Git policy are unchanged. No other issue is relaunched by this revision.

## Baseline evidence

The revision was based on repository `main` at `040f12a6d01d1fd90864037c464b8d5defbfcfe3`, where the T3 folder has 344 canonical files, zero missing/unexpected/hash-mismatched entries, and the catalog image-inventory digest matches. The designated PDF SHA-256 remains `1d9f0124a0c8ef759526decc90a1a410f694e2b7fa992b430fc413e783df85bc`.

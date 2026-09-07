# Plan

Planner: GPT-6 Astra. Execution: one user-launched Sol/Luna issue at a time.

| ID | Outcome | Model | Depends on |
|---|---|---|---|
| JPG-000 | Validate section records and page-batch helper compatibility | GPT-5.6 Sol | None |
| JPG-T1-INV | T1: verify source manifest and exact page ownership | GPT-5.6 Luna | None |
| JPG-T2-INV | T2: verify source manifest and exact page ownership | GPT-5.6 Luna | None |
| JPG-T3-INV | T3: verify source manifest and exact page ownership | GPT-5.6 Luna | None |
| JPG-W1-INV | W1: verify source manifest and exact page ownership | GPT-5.6 Luna | None |
| JPG-W2-INV | W2: verify source manifest and exact page ownership | GPT-5.6 Luna | None |
| JPG-T1-C002 | T1 pilot: convert physical 023-040 (chapter 01) | GPT-5.6 Sol | JPG-T1-INV, JPG-000 |
| JPG-T2-C001 | T2 pilot: convert physical 007-030 (chapter 21) | GPT-5.6 Sol | JPG-T2-INV, JPG-000 |
| JPG-T3-C001 | T3 pilot: convert physical 007-030 (chapter 33) | GPT-5.6 Sol | JPG-T3-INV, JPG-000 |
| JPG-W1-C002 | W1 pilot: convert physical 024-031 (chapter 01) | GPT-5.6 Sol | JPG-W1-INV, JPG-000 |
| JPG-W2-C001 | W2 pilot: convert physical 004-021 (chapter 21) | GPT-5.6 Sol | JPG-W2-INV, JPG-000 |
| JPG-T1-PILOT-QA | T1: review pilot and lock source-specific conventions | GPT-5.6 Sol | JPG-T1-C002 |
| JPG-T2-PILOT-QA | T2: review pilot and lock source-specific conventions | GPT-5.6 Sol | JPG-T2-C001 |
| JPG-T3-PILOT-QA | T3: review pilot and lock source-specific conventions | GPT-5.6 Sol | JPG-T3-C001 |
| JPG-W1-PILOT-QA | W1: review pilot and lock source-specific conventions | GPT-5.6 Sol | JPG-W1-C002 |
| JPG-W2-PILOT-QA | W2: review pilot and lock source-specific conventions | GPT-5.6 Sol | JPG-W2-C001 |
| JPG-T1-C001 | T1 convert physical 004-016 (chapter 00) | GPT-5.6 Sol | JPG-T1-INV, JPG-000, JPG-T1-PILOT-QA |
| JPG-T1-C003 | T1 convert physical 041-061 (chapter 02) | GPT-5.6 Sol | JPG-T1-INV, JPG-000, JPG-T1-PILOT-QA |
| JPG-T1-C004 | T1 convert physical 062-066 (chapter 02) | GPT-5.6 Sol | JPG-T1-INV, JPG-000, JPG-T1-PILOT-QA |
| JPG-T1-C005 | T1 convert physical 067-076 (chapter 03) | GPT-5.6 Sol | JPG-T1-INV, JPG-000, JPG-T1-PILOT-QA |
| JPG-T1-C006 | T1 convert physical 077-097 (chapter 04) | GPT-5.6 Sol | JPG-T1-INV, JPG-000, JPG-T1-PILOT-QA |
| JPG-T1-C007 | T1 convert physical 098-106 (chapter 04) | GPT-5.6 Sol | JPG-T1-INV, JPG-000, JPG-T1-PILOT-QA |
| JPG-T1-C008 | T1 convert physical 107-112 (chapter 05) | GPT-5.6 Sol | JPG-T1-INV, JPG-000, JPG-T1-PILOT-QA |
| JPG-T1-C009 | T1 convert physical 113-126 (chapter 06) | GPT-5.6 Sol | JPG-T1-INV, JPG-000, JPG-T1-PILOT-QA |
| JPG-T1-C010 | T1 convert physical 127-130 (chapter 07) | GPT-5.6 Sol | JPG-T1-INV, JPG-000, JPG-T1-PILOT-QA |
| JPG-T1-C011 | T1 convert physical 131-140 (chapter 08) | GPT-5.6 Sol | JPG-T1-INV, JPG-000, JPG-T1-PILOT-QA |
| JPG-T1-C012 | T1 convert physical 141-164 (chapter 08) | GPT-5.6 Sol | JPG-T1-INV, JPG-000, JPG-T1-PILOT-QA |
| JPG-T1-C013 | T1 convert physical 165-180 (chapter 09) | GPT-5.6 Sol | JPG-T1-INV, JPG-000, JPG-T1-PILOT-QA |
| JPG-T1-C014 | T1 convert physical 181-200 (chapter 10) | GPT-5.6 Sol | JPG-T1-INV, JPG-000, JPG-T1-PILOT-QA |
| JPG-T1-C015 | T1 convert physical 201-218 (chapter 11) | GPT-5.6 Sol | JPG-T1-INV, JPG-000, JPG-T1-PILOT-QA |
| JPG-T1-C016 | T1 convert physical 219-235 (chapter 12) | GPT-5.6 Sol | JPG-T1-INV, JPG-000, JPG-T1-PILOT-QA |
| JPG-T1-C017 | T1 convert physical 236-251 (chapter 12) | GPT-5.6 Sol | JPG-T1-INV, JPG-000, JPG-T1-PILOT-QA |
| JPG-T1-C018 | T1 convert physical 252-271 (chapter 12) | GPT-5.6 Sol | JPG-T1-INV, JPG-000, JPG-T1-PILOT-QA |
| JPG-T1-C019 | T1 convert physical 272-276 (chapter 12) | GPT-5.6 Sol | JPG-T1-INV, JPG-000, JPG-T1-PILOT-QA |
| JPG-T1-C020 | T1 convert physical 277-284 (chapter 13) | GPT-5.6 Sol | JPG-T1-INV, JPG-000, JPG-T1-PILOT-QA |
| JPG-T1-C021 | T1 convert physical 285-307 (chapter 14) | GPT-5.6 Sol | JPG-T1-INV, JPG-000, JPG-T1-PILOT-QA |
| JPG-T1-C022 | T1 convert physical 308-310 (chapter 14) | GPT-5.6 Sol | JPG-T1-INV, JPG-000, JPG-T1-PILOT-QA |
| JPG-T1-C023 | T1 convert physical 311-322 (chapter 15) | GPT-5.6 Sol | JPG-T1-INV, JPG-000, JPG-T1-PILOT-QA |
| JPG-T1-C024 | T1 convert physical 323-326 (chapter 16) | GPT-5.6 Sol | JPG-T1-INV, JPG-000, JPG-T1-PILOT-QA |
| JPG-T1-C025 | T1 convert physical 327-330 (chapter 17) | GPT-5.6 Sol | JPG-T1-INV, JPG-000, JPG-T1-PILOT-QA |
| JPG-T1-C026 | T1 convert physical 331-340 (chapter 18) | GPT-5.6 Sol | JPG-T1-INV, JPG-000, JPG-T1-PILOT-QA |
| JPG-T1-C027 | T1 convert physical 341-348 (chapter 19) | GPT-5.6 Sol | JPG-T1-INV, JPG-000, JPG-T1-PILOT-QA |
| JPG-T1-C028 | T1 convert physical 349-358 (chapter 20) | GPT-5.6 Sol | JPG-T1-INV, JPG-000, JPG-T1-PILOT-QA |
| JPG-T2-C002 | T2 convert physical 031-040 (chapter 21) | GPT-5.6 Sol | JPG-T2-INV, JPG-000, JPG-T2-PILOT-QA |
| JPG-T2-C003 | T2 convert physical 041-062 (chapter 22) | GPT-5.6 Sol | JPG-T2-INV, JPG-000, JPG-T2-PILOT-QA |
| JPG-T2-C004 | T2 convert physical 063-085 (chapter 23) | GPT-5.6 Sol | JPG-T2-INV, JPG-000, JPG-T2-PILOT-QA |
| JPG-T2-C005 | T2 convert physical 086-100 (chapter 23) | GPT-5.6 Sol | JPG-T2-INV, JPG-000, JPG-T2-PILOT-QA |
| JPG-T2-C006 | T2 convert physical 101-118 (chapter 24) | GPT-5.6 Sol | JPG-T2-INV, JPG-000, JPG-T2-PILOT-QA |
| JPG-T2-C007 | T2 convert physical 119-142 (chapter 24) | GPT-5.6 Sol | JPG-T2-INV, JPG-000, JPG-T2-PILOT-QA |
| JPG-T2-C008 | T2 convert physical 143-166 (chapter 25) | GPT-5.6 Sol | JPG-T2-INV, JPG-000, JPG-T2-PILOT-QA |
| JPG-T2-C009 | T2 convert physical 167-185 (chapter 26) | GPT-5.6 Sol | JPG-T2-INV, JPG-000, JPG-T2-PILOT-QA |
| JPG-T2-C010 | T2 convert physical 186-208 (chapter 26) | GPT-5.6 Sol | JPG-T2-INV, JPG-000, JPG-T2-PILOT-QA |
| JPG-T2-C011 | T2 convert physical 209-214 (chapter 26) | GPT-5.6 Sol | JPG-T2-INV, JPG-000, JPG-T2-PILOT-QA |
| JPG-T2-C012 | T2 convert physical 215-238 (chapter 27) | GPT-5.6 Sol | JPG-T2-INV, JPG-000, JPG-T2-PILOT-QA |
| JPG-T2-C013 | T2 convert physical 239-252 (chapter 27) | GPT-5.6 Sol | JPG-T2-INV, JPG-000, JPG-T2-PILOT-QA |
| JPG-T2-C014 | T2 convert physical 253-276 (chapter 28) | GPT-5.6 Sol | JPG-T2-INV, JPG-000, JPG-T2-PILOT-QA |
| JPG-T2-C015 | T2 convert physical 277-296 (chapter 28) | GPT-5.6 Sol | JPG-T2-INV, JPG-000, JPG-T2-PILOT-QA |
| JPG-T2-C016 | T2 convert physical 297-314 (chapter 29) | GPT-5.6 Sol | JPG-T2-INV, JPG-000, JPG-T2-PILOT-QA |
| JPG-T2-C017 | T2 convert physical 315-332 (chapter 29) | GPT-5.6 Sol | JPG-T2-INV, JPG-000, JPG-T2-PILOT-QA |
| JPG-T2-C018 | T2 convert physical 333-346 (chapter 29) | GPT-5.6 Sol | JPG-T2-INV, JPG-000, JPG-T2-PILOT-QA |
| JPG-T2-C019 | T2 convert physical 347-367 (chapter 30) | GPT-5.6 Sol | JPG-T2-INV, JPG-000, JPG-T2-PILOT-QA |
| JPG-T2-C020 | T2 convert physical 368-380 (chapter 30) | GPT-5.6 Sol | JPG-T2-INV, JPG-000, JPG-T2-PILOT-QA |
| JPG-T2-C021 | T2 convert physical 381-400 (chapter 31) | GPT-5.6 Sol | JPG-T2-INV, JPG-000, JPG-T2-PILOT-QA |
| JPG-T2-C022 | T2 convert physical 401-410 (chapter 31) | GPT-5.6 Sol | JPG-T2-INV, JPG-000, JPG-T2-PILOT-QA |
| JPG-T2-C023 | T2 convert physical 411-421 (chapter 32) | GPT-5.6 Sol | JPG-T2-INV, JPG-000, JPG-T2-PILOT-QA |
| JPG-T2-C024 | T2 convert physical 422-442 (chapter 32) | GPT-5.6 Sol | JPG-T2-INV, JPG-000, JPG-T2-PILOT-QA |
| JPG-T2-C025 | T2 convert physical 443-446 (chapter 32) | GPT-5.6 Sol | JPG-T2-INV, JPG-000, JPG-T2-PILOT-QA |
| JPG-T3-C002 | T3 convert physical 031-049 (chapter 33) | GPT-5.6 Sol | JPG-T3-INV, JPG-000, JPG-T3-PILOT-QA |
| JPG-T3-C003 | T3 convert physical 050-071 (chapter 33) | GPT-5.6 Sol | JPG-T3-INV, JPG-000, JPG-T3-PILOT-QA |
| JPG-T3-C004 | T3 convert physical 072-076 (chapter 33) | GPT-5.6 Sol | JPG-T3-INV, JPG-000, JPG-T3-PILOT-QA |
| JPG-T3-C005 | T3 convert physical 077-099 (chapter 34) | GPT-5.6 Sol | JPG-T3-INV, JPG-000, JPG-T3-PILOT-QA |
| JPG-T3-C006 | T3 convert physical 100-122 (chapter 34) | GPT-5.6 Sol | JPG-T3-INV, JPG-000, JPG-T3-PILOT-QA |
| JPG-T3-C007 | T3 convert physical 123-137 (chapter 35) | GPT-5.6 Sol | JPG-T3-INV, JPG-000, JPG-T3-PILOT-QA |
| JPG-T3-C008 | T3 convert physical 138-154 (chapter 35) | GPT-5.6 Sol | JPG-T3-INV, JPG-000, JPG-T3-PILOT-QA |
| JPG-T3-C009 | T3 convert physical 155-178 (chapter 35) | GPT-5.6 Sol | JPG-T3-INV, JPG-000, JPG-T3-PILOT-QA |
| JPG-T3-C010 | T3 convert physical 179-202 (chapter 36) | GPT-5.6 Sol | JPG-T3-INV, JPG-000, JPG-T3-PILOT-QA |
| JPG-T3-C011 | T3 convert physical 203-220 (chapter 37) | GPT-5.6 Sol | JPG-T3-INV, JPG-000, JPG-T3-PILOT-QA |
| JPG-T3-C012 | T3 convert physical 221-229 (chapter 38) | GPT-5.6 Sol | JPG-T3-INV, JPG-000, JPG-T3-PILOT-QA |
| JPG-T3-C013 | T3 convert physical 230-249 (chapter 38) | GPT-5.6 Sol | JPG-T3-INV, JPG-000, JPG-T3-PILOT-QA |
| JPG-T3-C014 | T3 convert physical 250-272 (chapter 38) | GPT-5.6 Sol | JPG-T3-INV, JPG-000, JPG-T3-PILOT-QA |
| JPG-T3-C015 | T3 convert physical 273-276 (chapter 38) | GPT-5.6 Sol | JPG-T3-INV, JPG-000, JPG-T3-PILOT-QA |
| JPG-T3-C016 | T3 convert physical 277-300 (chapter 39) | GPT-5.6 Sol | JPG-T3-INV, JPG-000, JPG-T3-PILOT-QA |
| JPG-T3-C017 | T3 convert physical 301-316 (chapter 39) | GPT-5.6 Sol | JPG-T3-INV, JPG-000, JPG-T3-PILOT-QA |
| JPG-T3-C018 | T3 convert physical 317-340 (chapter 40) | GPT-5.6 Sol | JPG-T3-INV, JPG-000, JPG-T3-PILOT-QA |
| JPG-W1-C001 | W1 convert physical 005-023 (chapter 00) | GPT-5.6 Sol | JPG-W1-INV, JPG-000, JPG-W1-PILOT-QA |
| JPG-W1-C003 | W1 convert physical 032-045 (chapter 02) | GPT-5.6 Sol | JPG-W1-INV, JPG-000, JPG-W1-PILOT-QA |
| JPG-W1-C004 | W1 convert physical 046-049 (chapter 03) | GPT-5.6 Sol | JPG-W1-INV, JPG-000, JPG-W1-PILOT-QA |
| JPG-W1-C005 | W1 convert physical 050-061 (chapter 04) | GPT-5.6 Sol | JPG-W1-INV, JPG-000, JPG-W1-PILOT-QA |
| JPG-W1-C006 | W1 convert physical 062-065 (chapter 05) | GPT-5.6 Sol | JPG-W1-INV, JPG-000, JPG-W1-PILOT-QA |
| JPG-W1-C007 | W1 convert physical 066-071 (chapter 06) | GPT-5.6 Sol | JPG-W1-INV, JPG-000, JPG-W1-PILOT-QA |
| JPG-W1-C008 | W1 convert physical 072-073 (chapter 07) | GPT-5.6 Sol | JPG-W1-INV, JPG-000, JPG-W1-PILOT-QA |
| JPG-W1-C009 | W1 convert physical 074-083 (chapter 08) | GPT-5.6 Sol | JPG-W1-INV, JPG-000, JPG-W1-PILOT-QA |
| JPG-W1-C010 | W1 convert physical 084-093 (chapter 09) | GPT-5.6 Sol | JPG-W1-INV, JPG-000, JPG-W1-PILOT-QA |
| JPG-W1-C011 | W1 convert physical 094-103 (chapter 10) | GPT-5.6 Sol | JPG-W1-INV, JPG-000, JPG-W1-PILOT-QA |
| JPG-W1-C012 | W1 convert physical 104-107 (chapter 11) | GPT-5.6 Sol | JPG-W1-INV, JPG-000, JPG-W1-PILOT-QA |
| JPG-W1-C013 | W1 convert physical 108-127 (chapter 12) | GPT-5.6 Sol | JPG-W1-INV, JPG-000, JPG-W1-PILOT-QA |
| JPG-W1-C014 | W1 convert physical 128-149 (chapter 12) | GPT-5.6 Sol | JPG-W1-INV, JPG-000, JPG-W1-PILOT-QA |
| JPG-W1-C015 | W1 convert physical 150-151 (chapter 13) | GPT-5.6 Sol | JPG-W1-INV, JPG-000, JPG-W1-PILOT-QA |
| JPG-W1-C016 | W1 convert physical 152-165 (chapter 14) | GPT-5.6 Sol | JPG-W1-INV, JPG-000, JPG-W1-PILOT-QA |
| JPG-W1-C017 | W1 convert physical 166-175 (chapter 15) | GPT-5.6 Sol | JPG-W1-INV, JPG-000, JPG-W1-PILOT-QA |
| JPG-W1-C018 | W1 convert physical 176-181 (chapter 16) | GPT-5.6 Sol | JPG-W1-INV, JPG-000, JPG-W1-PILOT-QA |
| JPG-W1-C019 | W1 convert physical 182-183 (chapter 17) | GPT-5.6 Sol | JPG-W1-INV, JPG-000, JPG-W1-PILOT-QA |
| JPG-W1-C020 | W1 convert physical 184-189 (chapter 18) | GPT-5.6 Sol | JPG-W1-INV, JPG-000, JPG-W1-PILOT-QA |
| JPG-W1-C021 | W1 convert physical 190-193 (chapter 19) | GPT-5.6 Sol | JPG-W1-INV, JPG-000, JPG-W1-PILOT-QA |
| JPG-W1-C022 | W1 convert physical 194-201 (chapter 20) | GPT-5.6 Sol | JPG-W1-INV, JPG-000, JPG-W1-PILOT-QA |
| JPG-W2-C002 | W2 convert physical 022-035 (chapter 22) | GPT-5.6 Sol | JPG-W2-INV, JPG-000, JPG-W2-PILOT-QA |
| JPG-W2-C003 | W2 convert physical 036-057 (chapter 23) | GPT-5.6 Sol | JPG-W2-INV, JPG-000, JPG-W2-PILOT-QA |
| JPG-W2-C004 | W2 convert physical 058-075 (chapter 24) | GPT-5.6 Sol | JPG-W2-INV, JPG-000, JPG-W2-PILOT-QA |
| JPG-W2-C005 | W2 convert physical 076-089 (chapter 25) | GPT-5.6 Sol | JPG-W2-INV, JPG-000, JPG-W2-PILOT-QA |
| JPG-W2-C006 | W2 convert physical 090-109 (chapter 26) | GPT-5.6 Sol | JPG-W2-INV, JPG-000, JPG-W2-PILOT-QA |
| JPG-W2-C007 | W2 convert physical 110-115 (chapter 26) | GPT-5.6 Sol | JPG-W2-INV, JPG-000, JPG-W2-PILOT-QA |
| JPG-W2-C008 | W2 convert physical 116-137 (chapter 27) | GPT-5.6 Sol | JPG-W2-INV, JPG-000, JPG-W2-PILOT-QA |
| JPG-W2-C009 | W2 convert physical 138-157 (chapter 28) | GPT-5.6 Sol | JPG-W2-INV, JPG-000, JPG-W2-PILOT-QA |
| JPG-W2-C010 | W2 convert physical 158-175 (chapter 29) | GPT-5.6 Sol | JPG-W2-INV, JPG-000, JPG-W2-PILOT-QA |
| JPG-W2-C011 | W2 convert physical 176-195 (chapter 30) | GPT-5.6 Sol | JPG-W2-INV, JPG-000, JPG-W2-PILOT-QA |
| JPG-W2-C012 | W2 convert physical 196-209 (chapter 31) | GPT-5.6 Sol | JPG-W2-INV, JPG-000, JPG-W2-PILOT-QA |
| JPG-W2-C013 | W2 convert physical 210-229 (chapter 32) | GPT-5.6 Sol | JPG-W2-INV, JPG-000, JPG-W2-PILOT-QA |
| JPG-W2-C014 | W2 convert physical 230-249 (chapter 33) | GPT-5.6 Sol | JPG-W2-INV, JPG-000, JPG-W2-PILOT-QA |
| JPG-W2-C015 | W2 convert physical 250-263 (chapter 33) | GPT-5.6 Sol | JPG-W2-INV, JPG-000, JPG-W2-PILOT-QA |
| JPG-W2-C016 | W2 convert physical 264-275 (chapter 34) | GPT-5.6 Sol | JPG-W2-INV, JPG-000, JPG-W2-PILOT-QA |
| JPG-W2-C017 | W2 convert physical 276-295 (chapter 35) | GPT-5.6 Sol | JPG-W2-INV, JPG-000, JPG-W2-PILOT-QA |
| JPG-W2-C018 | W2 convert physical 296-303 (chapter 35) | GPT-5.6 Sol | JPG-W2-INV, JPG-000, JPG-W2-PILOT-QA |
| JPG-W2-C019 | W2 convert physical 304-315 (chapter 36) | GPT-5.6 Sol | JPG-W2-INV, JPG-000, JPG-W2-PILOT-QA |
| JPG-W2-C020 | W2 convert physical 316-323 (chapter 37) | GPT-5.6 Sol | JPG-W2-INV, JPG-000, JPG-W2-PILOT-QA |
| JPG-W2-C021 | W2 convert physical 324-343 (chapter 38) | GPT-5.6 Sol | JPG-W2-INV, JPG-000, JPG-W2-PILOT-QA |
| JPG-W2-C022 | W2 convert physical 344-363 (chapter 39) | GPT-5.6 Sol | JPG-W2-INV, JPG-000, JPG-W2-PILOT-QA |
| JPG-W2-C023 | W2 convert physical 364-371 (chapter 39) | GPT-5.6 Sol | JPG-W2-INV, JPG-000, JPG-W2-PILOT-QA |
| JPG-W2-C024 | W2 convert physical 372-389 (chapter 40) | GPT-5.6 Sol | JPG-W2-INV, JPG-000, JPG-W2-PILOT-QA |
| JPG-W2-C025 | W2 convert physical 390-395 (chapter 41) | GPT-5.6 Sol | JPG-W2-INV, JPG-000, JPG-W2-PILOT-QA |
| JPG-T1-QA01 | T1: chapter completeness QA 00 | GPT-5.6 Sol | JPG-T1-C001, JPG-T1-PILOT-QA |
| JPG-T1-QA02 | T1: chapter completeness QA 01, 02 | GPT-5.6 Sol | JPG-T1-C002, JPG-T1-C003, JPG-T1-C004, JPG-T1-PILOT-QA |
| JPG-T1-QA03 | T1: chapter completeness QA 03, 04, 05 | GPT-5.6 Sol | JPG-T1-C005, JPG-T1-C006, JPG-T1-C007, JPG-T1-C008, JPG-T1-PILOT-QA |
| JPG-T1-QA04 | T1: chapter completeness QA 06, 07 | GPT-5.6 Sol | JPG-T1-C009, JPG-T1-C010, JPG-T1-PILOT-QA |
| JPG-T1-QA05 | T1: chapter completeness QA 08 | GPT-5.6 Sol | JPG-T1-C011, JPG-T1-C012, JPG-T1-PILOT-QA |
| JPG-T1-QA06 | T1: chapter completeness QA 09, 10 | GPT-5.6 Sol | JPG-T1-C013, JPG-T1-C014, JPG-T1-PILOT-QA |
| JPG-T1-QA07 | T1: chapter completeness QA 11 | GPT-5.6 Sol | JPG-T1-C015, JPG-T1-PILOT-QA |
| JPG-T1-QA08 | T1: chapter completeness QA 12 | GPT-5.6 Sol | JPG-T1-C016, JPG-T1-C017, JPG-T1-C018, JPG-T1-C019, JPG-T1-PILOT-QA |
| JPG-T1-QA09 | T1: chapter completeness QA 13, 14, 15 | GPT-5.6 Sol | JPG-T1-C020, JPG-T1-C021, JPG-T1-C022, JPG-T1-C023, JPG-T1-PILOT-QA |
| JPG-T1-QA10 | T1: chapter completeness QA 16, 17, 18, 19, 20 | GPT-5.6 Sol | JPG-T1-C024, JPG-T1-C025, JPG-T1-C026, JPG-T1-C027, JPG-T1-C028, JPG-T1-PILOT-QA |
| JPG-T2-QA01 | T2: chapter completeness QA 21 | GPT-5.6 Sol | JPG-T2-C001, JPG-T2-C002, JPG-T2-PILOT-QA |
| JPG-T2-QA02 | T2: chapter completeness QA 22 | GPT-5.6 Sol | JPG-T2-C003, JPG-T2-PILOT-QA |
| JPG-T2-QA03 | T2: chapter completeness QA 23 | GPT-5.6 Sol | JPG-T2-C004, JPG-T2-C005, JPG-T2-PILOT-QA |
| JPG-T2-QA04 | T2: chapter completeness QA 24 | GPT-5.6 Sol | JPG-T2-C006, JPG-T2-C007, JPG-T2-PILOT-QA |
| JPG-T2-QA05 | T2: chapter completeness QA 25 | GPT-5.6 Sol | JPG-T2-C008, JPG-T2-PILOT-QA |
| JPG-T2-QA06 | T2: chapter completeness QA 26 | GPT-5.6 Sol | JPG-T2-C009, JPG-T2-C010, JPG-T2-C011, JPG-T2-PILOT-QA |
| JPG-T2-QA07 | T2: chapter completeness QA 27 | GPT-5.6 Sol | JPG-T2-C012, JPG-T2-C013, JPG-T2-PILOT-QA |
| JPG-T2-QA08 | T2: chapter completeness QA 28 | GPT-5.6 Sol | JPG-T2-C014, JPG-T2-C015, JPG-T2-PILOT-QA |
| JPG-T2-QA09 | T2: chapter completeness QA 29 | GPT-5.6 Sol | JPG-T2-C016, JPG-T2-C017, JPG-T2-C018, JPG-T2-PILOT-QA |
| JPG-T2-QA10 | T2: chapter completeness QA 30 | GPT-5.6 Sol | JPG-T2-C019, JPG-T2-C020, JPG-T2-PILOT-QA |
| JPG-T2-QA11 | T2: chapter completeness QA 31 | GPT-5.6 Sol | JPG-T2-C021, JPG-T2-C022, JPG-T2-PILOT-QA |
| JPG-T2-QA12 | T2: chapter completeness QA 32 | GPT-5.6 Sol | JPG-T2-C023, JPG-T2-C024, JPG-T2-C025, JPG-T2-PILOT-QA |
| JPG-T3-QA01 | T3: chapter completeness QA 33 | GPT-5.6 Sol | JPG-T3-C001, JPG-T3-C002, JPG-T3-C003, JPG-T3-C004, JPG-T3-PILOT-QA |
| JPG-T3-QA02 | T3: chapter completeness QA 34 | GPT-5.6 Sol | JPG-T3-C005, JPG-T3-C006, JPG-T3-PILOT-QA |
| JPG-T3-QA03 | T3: chapter completeness QA 35 | GPT-5.6 Sol | JPG-T3-C007, JPG-T3-C008, JPG-T3-C009, JPG-T3-PILOT-QA |
| JPG-T3-QA04 | T3: chapter completeness QA 36, 37 | GPT-5.6 Sol | JPG-T3-C010, JPG-T3-C011, JPG-T3-PILOT-QA |
| JPG-T3-QA05 | T3: chapter completeness QA 38 | GPT-5.6 Sol | JPG-T3-C012, JPG-T3-C013, JPG-T3-C014, JPG-T3-C015, JPG-T3-PILOT-QA |
| JPG-T3-QA06 | T3: chapter completeness QA 39 | GPT-5.6 Sol | JPG-T3-C016, JPG-T3-C017, JPG-T3-PILOT-QA |
| JPG-T3-QA07 | T3: chapter completeness QA 40 | GPT-5.6 Sol | JPG-T3-C018, JPG-T3-PILOT-QA |
| JPG-W1-QA01 | W1: chapter completeness QA 00, 01, 02, 03 | GPT-5.6 Sol | JPG-W1-C001, JPG-W1-C002, JPG-W1-C003, JPG-W1-C004, JPG-W1-PILOT-QA |
| JPG-W1-QA02 | W1: chapter completeness QA 04, 05, 06, 07, 08, 09 | GPT-5.6 Sol | JPG-W1-C005, JPG-W1-C006, JPG-W1-C007, JPG-W1-C008, JPG-W1-C009, JPG-W1-C010, JPG-W1-PILOT-QA |
| JPG-W1-QA03 | W1: chapter completeness QA 10, 11 | GPT-5.6 Sol | JPG-W1-C011, JPG-W1-C012, JPG-W1-PILOT-QA |
| JPG-W1-QA04 | W1: chapter completeness QA 12, 13 | GPT-5.6 Sol | JPG-W1-C013, JPG-W1-C014, JPG-W1-C015, JPG-W1-PILOT-QA |
| JPG-W1-QA05 | W1: chapter completeness QA 14, 15, 16, 17, 18, 19 | GPT-5.6 Sol | JPG-W1-C016, JPG-W1-C017, JPG-W1-C018, JPG-W1-C019, JPG-W1-C020, JPG-W1-C021, JPG-W1-PILOT-QA |
| JPG-W1-QA06 | W1: chapter completeness QA 20 | GPT-5.6 Sol | JPG-W1-C022, JPG-W1-PILOT-QA |
| JPG-W2-QA01 | W2: chapter completeness QA 21, 22 | GPT-5.6 Sol | JPG-W2-C001, JPG-W2-C002, JPG-W2-PILOT-QA |
| JPG-W2-QA02 | W2: chapter completeness QA 23, 24 | GPT-5.6 Sol | JPG-W2-C003, JPG-W2-C004, JPG-W2-PILOT-QA |
| JPG-W2-QA03 | W2: chapter completeness QA 25, 26 | GPT-5.6 Sol | JPG-W2-C005, JPG-W2-C006, JPG-W2-C007, JPG-W2-PILOT-QA |
| JPG-W2-QA04 | W2: chapter completeness QA 27, 28 | GPT-5.6 Sol | JPG-W2-C008, JPG-W2-C009, JPG-W2-PILOT-QA |
| JPG-W2-QA05 | W2: chapter completeness QA 29, 30 | GPT-5.6 Sol | JPG-W2-C010, JPG-W2-C011, JPG-W2-PILOT-QA |
| JPG-W2-QA06 | W2: chapter completeness QA 31, 32 | GPT-5.6 Sol | JPG-W2-C012, JPG-W2-C013, JPG-W2-PILOT-QA |
| JPG-W2-QA07 | W2: chapter completeness QA 33, 34 | GPT-5.6 Sol | JPG-W2-C014, JPG-W2-C015, JPG-W2-C016, JPG-W2-PILOT-QA |
| JPG-W2-QA08 | W2: chapter completeness QA 35, 36, 37 | GPT-5.6 Sol | JPG-W2-C017, JPG-W2-C018, JPG-W2-C019, JPG-W2-C020, JPG-W2-PILOT-QA |
| JPG-W2-QA09 | W2: chapter completeness QA 38, 39 | GPT-5.6 Sol | JPG-W2-C021, JPG-W2-C022, JPG-W2-C023, JPG-W2-PILOT-QA |
| JPG-W2-QA10 | W2: chapter completeness QA 40, 41 | GPT-5.6 Sol | JPG-W2-C024, JPG-W2-C025, JPG-W2-PILOT-QA |
| JPG-T1-ASSEMBLE | T1: aggregate reviewed tasks and assemble clean Markdown | GPT-5.6 Luna | JPG-T1-QA01, JPG-T1-QA02, JPG-T1-QA03, JPG-T1-QA04, JPG-T1-QA05, JPG-T1-QA06, JPG-T1-QA07, JPG-T1-QA08, JPG-T1-QA09, JPG-T1-QA10 |
| JPG-T2-ASSEMBLE | T2: aggregate reviewed tasks and assemble clean Markdown | GPT-5.6 Luna | JPG-T2-QA01, JPG-T2-QA02, JPG-T2-QA03, JPG-T2-QA04, JPG-T2-QA05, JPG-T2-QA06, JPG-T2-QA07, JPG-T2-QA08, JPG-T2-QA09, JPG-T2-QA10, JPG-T2-QA11, JPG-T2-QA12 |
| JPG-T3-ASSEMBLE | T3: aggregate reviewed tasks and assemble clean Markdown | GPT-5.6 Luna | JPG-T3-QA01, JPG-T3-QA02, JPG-T3-QA03, JPG-T3-QA04, JPG-T3-QA05, JPG-T3-QA06, JPG-T3-QA07 |
| JPG-W1-ASSEMBLE | W1: aggregate reviewed tasks and assemble clean Markdown | GPT-5.6 Luna | JPG-W1-QA01, JPG-W1-QA02, JPG-W1-QA03, JPG-W1-QA04, JPG-W1-QA05, JPG-W1-QA06 |
| JPG-W2-ASSEMBLE | W2: aggregate reviewed tasks and assemble clean Markdown | GPT-5.6 Luna | JPG-W2-QA01, JPG-W2-QA02, JPG-W2-QA03, JPG-W2-QA04, JPG-W2-QA05, JPG-W2-QA06, JPG-W2-QA07, JPG-W2-QA08, JPG-W2-QA09, JPG-W2-QA10 |
| JPG-T1-ACCEPT | T1: accept final source and merged-text handoff | GPT-5.6 Sol | JPG-T1-ASSEMBLE |
| JPG-T2-ACCEPT | T2: accept final source and merged-text handoff | GPT-5.6 Sol | JPG-T2-ASSEMBLE |
| JPG-T3-ACCEPT | T3: accept final source and merged-text handoff | GPT-5.6 Sol | JPG-T3-ASSEMBLE |
| JPG-W1-ACCEPT | W1: accept final source and merged-text handoff | GPT-5.6 Sol | JPG-W1-ASSEMBLE |
| JPG-W2-ACCEPT | W2: accept final source and merged-text handoff | GPT-5.6 Sol | JPG-W2-ASSEMBLE |
| JPG-HANDOFF | Verify five independent Markdown handoffs and publish their index | GPT-5.6 Luna | JPG-T1-ACCEPT, JPG-T2-ACCEPT, JPG-T3-ACCEPT, JPG-W1-ACCEPT, JPG-W2-ACCEPT |

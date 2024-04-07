# Copyright (c) 2022-2024, Keivan Tafakkori. All rights reserved.
# See the file LICENSE file for licensing details.

from feloopy import madm

m = madm("cilos", "cilos_model", "pydecision")
m.add_dm(
    [
        [250, 16, 12, 5],
        [200, 16, 8, 3],
        [300, 32, 16, 4],
        [275, 32, 8, 4],
        [225, 16, 16, 2],
    ]
)
m.sol(["min", "max", "max", "max"])
m.report(show_tensors=True)

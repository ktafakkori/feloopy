import feloopy as flp

# Define a model
m = flp.madm("ahp", "ahp_model", "pydecision")

# Define criteria pairwise comparison matrix
m.add_cpcm(
    [
        [1, 1 / 3, 1 / 5, 1, 1 / 4, 1 / 2, 3],
        [3, 1, 1 / 2, 2, 1 / 3, 3, 3],
        [5, 2, 1, 4, 5, 6, 5],
        [1, 1 / 2, 1 / 4, 1, 1 / 4, 1, 2],
        [4, 3, 1 / 5, 4, 1, 3, 2],
        [2, 1 / 3, 1 / 6, 1, 1 / 3, 1, 1 / 3],
        [1 / 3, 1 / 3, 1 / 5, 1 / 2, 1 / 2, 3, 1],
    ]
)

# Define solve method
m.sol()

# Report the results
m.report(show_tensors=True)

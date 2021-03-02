# Great learning tool. I'll explain how this works.

def storage_calculator(filesize):
    block_size = 4096

    # The floor division takes the FIRST NUMBER.
    # IF filesize < block_size, the value of full_block = 0
    full_blocks = filesize // block_size

    remainder = filesize % block_size

    # If filesize is not FULLY DIVISIBLE by block_size,
    # The If bloc WILL run.
    if remainder > 0:
        return full_blocks * block_size + block_size
    return full_blocks * block_size


print(calculate_storage(1))  # 'If bloc' runs
print(calculate_storage(4095))  # 'If bloc' runs
print(calculate_storage(4096))  # 'If bloc' does not run
print(calculate_storage(8192))  # 'If bloc' does not run

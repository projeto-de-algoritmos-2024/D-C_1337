class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        def update(index: int, value: int, tree: List[int], size: int) -> None:

            index += 1
            while index <= size:
                tree[index] += value
                index += index & (-index)

        def query(index: int, tree: List[int]) -> int:
            index += 1
            total = 0
            while index > 0:
                total += tree[index]
                index -= index & (-index)
            return total

        if not nums:
            return []


        sorted_set = sorted(set(nums))
        rank_map = {num: i for i, num in enumerate(sorted_set)}

        n = len(sorted_set)
        bit = [0] * (n + 1)

        result = []
        for num in reversed(nums):
            rank = rank_map[num]
            result.append(query(rank - 1, bit))
            update(rank, 1, bit, n)

        return result[::-1]
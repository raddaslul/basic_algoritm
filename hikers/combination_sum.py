from typing import List


class Solution:
    def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
        answer = []

        # 주어진 target에 candidates로 주어진 원소들을 빼나가면서 0이 나오면 정답에 추가하는 식으로 로직 구현
        # 원소들의 조합의 합이 target이 되는지를 판단해야 하기 때문에 dfs를 이용
        def dfs(cur_sum, cur_index, sub_answer):
            # target에서 candidates로 주어진 원소들을 뺐는데 음수가 나오면 탈출
            if cur_sum < 0:
                return
            # target에서 candidates로 주어진 원소들을 뺐는데 0이 나오면 정답에 추가하면서 탈출
            elif cur_sum == 0:
                answer.append(sub_answer)
                return

            # candidates에 주어진 값들이 중복 가능하다고 했기 때문에 dfs로 중복된 원소들의 합까지 확인
            for index in range(cur_index, len(candidates)):
                dfs(cur_sum - candidates[index], index, sub_answer + [candidates[index]])

        dfs(target, 0, [])
        return answer

    result = combinationSum(candidates=[2, 3, 6, 7], target=7)
    print(result)

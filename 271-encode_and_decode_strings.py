class Solution:
  def encode(self, strs: list[str]) -> str:
    return ':;'.join(strs) if strs else None

  def decode(self, s: str) -> list[str]:
    return s.split(':;') if s is not None else []
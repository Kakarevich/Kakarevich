- 👋 Hi World, I’m @Kakarevich
- 👀 I’m interested in Computer techologies.
- 🌱 I’m currently learning ...
- 💞️ I’m looking to collaborate on ...
- 📫 How to reach me ...

<!---
Kakarevich/Kakarevich is a ✨ special ✨ repository because its `README.md` (this file) appears on your GitHub profile.
You can click the Preview link to take a look at your changes.
--->


bool isEmpty(){  
  if(this->data == 0)
    return true;
  bool result = true;
  for (int i = 0; i < 10; i++) {
    if(readFromFile("input.txt", i)) {
      result = indexes[i].matched;
    }
    indexes[i].setMatched(true);
  }
  return result;
}

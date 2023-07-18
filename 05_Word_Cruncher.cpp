#include <iostream>
#include <vector>
#include <unordered_set>
#include <algorithm>

using namespace std;

vector<string> results;

void dfs(const vector<string>& words, const string& target, vector<int>& path, int start, unordered_set<int>& used) {
    if (start == target.size()) {
        string result;
        for (int i : path) {
            result += words[i] + " ";
        }
        if (std::find(results.begin(), results.end(), result) == results.end()) {
        results.push_back(result);
        }

        return;
    }
    for (int i = 0; i < words.size(); i++) {
        if (used.find(i) == used.end() && target.substr(start, words[i].size()) == words[i]) {
            used.insert(i);
            path.push_back(i);
            dfs(words, target, path, start + words[i].size(), used);
            path.pop_back();
            used.erase(i);
        }
    }
}

vector<string> word_cruncher(const vector<string>& words, const string& target) {
    results.clear();
    vector<int> path;
    unordered_set<int> used;
    dfs(words, target, path, 0, used);
    return results;
}

int main() {
    vector<string> words;
    string target;

    string input;
    getline(cin, input);
    size_t pos = 0;
    while ((pos = input.find(", ")) != string::npos) {
        words.push_back(input.substr(0, pos));
        input.erase(0, pos + 2);
    }
    words.push_back(input);

    getline(cin, target);

    vector<string> result = word_cruncher(words, target);
    for (const string& res : result) {
        cout << res << endl;
    }

    return 0;
}

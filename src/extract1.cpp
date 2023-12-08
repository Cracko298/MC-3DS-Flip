#include <iostream>
#include <fstream>
#include <algorithm>

using namespace std;

int main(int argc, char** argv) {
    if (argc != 2) {
        cerr << "Usage: " << ".\\extract_lines.exe" << " <image_path>" << "\n" << endl;
        return 1;
    }

    string image_path = argv[1];

    ifstream file(image_path, ios::binary);
    if (!file.is_open()) {
        cerr << "Error opening file: " << image_path << "\n" << endl;
        return 1;
    }

    size_t dotIndex = image_path.find_last_of(".");
    string out_path = image_path.substr(0, dotIndex) + "_firstline" + image_path.substr(dotIndex);

    if (dotIndex == string::npos || image_path.substr(dotIndex) != ".3dst") {
        cerr << "Error: The provided file is not an '.3dst' image.\n" << endl;
        return 1;
    }

    file.seekg(0x20, ios::cur);

    ofstream outFile(out_path, ios::binary | ios::out);
    if (!outFile.is_open()) {
        cerr << "Error creating output file: " << out_path << "\n" << endl;
        return 1;
    }

    for (int i = 0; i < 8; ++i) {
        string data1(0x08, '\0');
        file.read(&data1[0], 0x08);
        cout << data1;
        file.seekg(0x08, ios::cur);

        string data2(0x08, '\0');
        file.read(&data2[0], 0x08);
        file.seekg(0x28, ios::cur);

        string data3(0x08, '\0');
        file.read(&data3[0], 0x08);
        file.seekg(0x08, ios::cur);

        string data4(0x08, '\0');
        file.read(&data4[0], 0x08);
        file.seekg(0xA8, ios::cur);

        outFile.write(data1.c_str(), 0x08);
        outFile.write(data2.c_str(), 0x08);
        outFile.write(data3.c_str(), 0x08);
        outFile.write(data4.c_str(), 0x08);
    }

    return 0;
}

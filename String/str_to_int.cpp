// 输入一个由数字组成的字符串，把它转换成整数并输出。例如：输入字符串"123"，输出整数123。
// 给定函数原型int StrToInt(const char *str) ，实现字符串转换成整数的功能，不能使用库函数atoi。

// 1.nullptr 2.+,- 3.illegal signal 4.out of range 5.space
#include <iostream>
#include <locale>
#include <string>
#include <cstdio>
using namespace std;

int StrToInt(const char* str, int len){
	static const int MAX_INT = (int)((unsigned)~0 >> 1);
	static const int MIN_INT = -(int)((unsigned)~0 >> 1) - 1;
	unsigned int ans = 0;

	if (*str == '\0'){
		return 0;
	}

	while (isspace(*str)){
		str++;
	}

	int sign = 1;
	if (*str == '+' || *str == '-'){
		if (*str == '-'){
			sign = -1;
		}
		str++;
	}

	while (*str != '\0'){
		if (isdigit(*str)){
			int c = *str - '0';
			if (sign > 0 && (ans > MAX_INT / 10 || (ans == MAX_INT / 10 && c > MAX_INT % 10))){
				ans = MAX_INT;
				break;
			}
			else if (sign < 0 && (ans > (unsigned)MIN_INT / 10 || (ans == (unsigned)MIN_INT / 10 && c > (unsigned)MIN_INT % 10))){
				ans = MIN_INT;
				break;
			}
			ans = ans * 10 + c;
		}
		str++;
	}
	return sign > 0 ? ans : -ans;
}

int main(){
	char s[] = "-a2b4c56h888999";
	cout << StrToInt(s, (sizeof(s)/sizeof(*s)-1)) << endl;
	return 0;
}
func strStr(haystack string, needle string) int {
    if len(haystack) < len(needle) {
        return -1
    }

    length := len(needle)

    for i := 0; i <= len(haystack) - length; i++ {
        if haystack[i: i + length] == needle {
            return i
        }
    }

    return -1
}
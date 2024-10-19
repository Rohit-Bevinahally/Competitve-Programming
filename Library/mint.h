struct mint{
    ll v; explicit operator ll() const { return v; }
    mint() { v = 0; }
    mint(ll _v) {
        v = (-mod < _v && _v < mod) ? _v : _v % mod;
        if (v < 0) v += mod; }
    friend bool operator==(const mint& a, const mint& b) {
        return a.v == b.v; }
    friend bool operator!=(const mint& a, const mint& b) {
        return !(a == b); }
    friend bool operator<(const mint& a, const mint& b) {
        return a.v < b.v; }
    mint& operator+=(const mint& m) {
        if ((v += m.v) >= mod) v -= mod;
        return *this; }
    mint& operator-=(const mint& m) {
        if ((v -= m.v) < 0) v += mod;
        return *this; }
    mint& operator*=(const mint& m) {
        v = v*m.v%mod; return *this; }
    mint& operator/=(const mint& m) { return (*this) *= inv(m); }
    mint& operator++() { return *this += 1; }
    mint& operator--() { return *this -= 1; }
    mint operator++(int) { mint temp = *this; ++*this; return temp; }
    mint operator--(int) { mint temp = *this; --*this; return temp; }
    mint operator-() const { return mint(-v); }
    friend mint operator+(mint a, const mint& b) { return a += b; }
    friend mint operator-(mint a, const mint& b) { return a -= b; }
    friend mint operator*(mint a, const mint& b) { return a *= b; }
    friend mint operator/(mint a, const mint& b) { return a /= b; }
    friend mint pow(mint a, ll p) {
        mint ans = 1; assert(p >= 0);
        for (; p; p /= 2, a *= a) if (p&1) ans *= a;
        return ans; }
    friend mint inv(const mint& a) { assert(a.v != 0);
        return pow(a,mod-2); }
    friend ostream& operator<<(ostream& os, const mint& m) {
        os << m.v; return os; }
    friend istream& operator>>(istream& is, mint& m) {
        ll x; is >> x;
        m.v = x;
        return is; }
};

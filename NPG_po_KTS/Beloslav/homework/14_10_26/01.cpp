int main () {
  led |= (1 << 3) | (1 << 5);

    led &= ~(1 << 2);

    if (led & (1 << 7)) {
        cout << "";
        return 0
    }
}
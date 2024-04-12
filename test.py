import win32com.client
import win32print

def print_docx_silently(file_path):
    """Prints a docx file silently in the background.

    Args:
        file_path (str): The path to the docx file.
    """

    word = win32com.client.Dispatch("Word.Application")
    word.Visible = False  # Hide Word application window

    doc = word.Documents.Open(file_path)

    # Set printer properties for silent printing (adjust as needed)
    printer = word.ActivePrinter
    word.ActivePrinter = printer + f" on {win32print.GetDefaultPrinter()}"  # Replace "Ne00:" with your printer name
    word.Options.PrintBackground = False  # Disable background printing

    doc.PrintOut()  # Print the document

    doc.Close()
    word.Quit()

if __name__ == "__main__":
    file_path = "c://Users//parmo//Documents//GitHub//HealStream//temp.docx"  # Replace with the actual file path
    print_docx_silently(file_path)
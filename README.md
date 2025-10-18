# Calculator with Tkinter  
A flexible and simple calculator built using **Python** and **Tkinter** for the graphical interface.

## Overview  
This project provides a straightforward graphical calculator application — perfect for learning, customization, and experimentation.  
- Main file: `MAIN.py` — the entry point of the application.  
- Interface & logic: `window.py` — contains the Tkinter visual components and arithmetic logic.  
- Folder `scratches/` — prototypes and test scripts used during development.  
- Known limitation: does not support complex numbers or infinite values.

## Why was this made?
- Learning **Python GUI development** using Tkinter.  
- Perfect playground to experiment with Tkinter widgets and GUI logic.
- It is a flexible and quick calculator: Capable of calculating the values of expressions containing more than one operation.

## Technologies Used  
- Python
- Tkinter (standard Python GUI library)  

## How to Run  
1. Clone the repository:  
   ```bash
   git clone https://github.com/pl1an/calculator_with_tkinter.git
   ```  
2. Move into the project folder:  
   ```bash
   cd calculator_with_tkinter
   ```  
3. Run the main script:  
   ```bash
   python MAIN.py
   ```  
4. The calculator window will open.

## Project Structure  
```
calculator_with_tkinter/
├── MAIN.py          # Main script that launches the GUI
├── window.py        # Defines widgets and calculator logic
├── scratches/       # Prototypes and experimental scripts
└── README.md        # This file
```

## Future updates
- Add support for **complex numbers** or **scientific notation**.  
- Implement a **calculation history** feature.  
- Add **keyboard shortcuts**.
- Introduce **themes** or customizable color palettes.  
- Refactor the logic to use a safer and more robust expression parser.  
- Package it into an executable using **PyInstaller** for distribution.

## 🚧 Known Limitations  
- Does not support complex or infinite numbers.  
- Basic GUI layout — may not scale well on all screens.  
- Potential risks of using Python’s `eval()` for composite expressions.

## License  
You are free to use, modify, and distribute this project. If no explicit license file is present, please reach out to the maintainer before including it in larger projects.

## Sources
- [https://realpython.com/python-gui-tkinter/](https://realpython.com/python-gui-tkinter/)

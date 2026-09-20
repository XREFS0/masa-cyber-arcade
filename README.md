# MASA Cyber Arcade Hub

A dual-module graphical arcade client combining competitive Rock-Paper-Scissors against computer agents and a grid-based Tic-Tac-Toe engine.

## Technical Architecture

The codebase follows modular software engineering patterns and OOP structure, designed for reliability, high maintainability, and clean separation of concerns:

- **Component Layering**: User interface and computational state are decoupled into specialized controllers and event loops.
- **Defensive Engineering**: Comprehensive validation guards protect against malformed inputs and runtime exceptions.
- **Modern Design Tokens**: Designed with a high-contrast dark aesthetic adhering to modern developer tooling visual standards.


## Preview

![Application Interface](screenshots/app_interface.png)
## Features

- Unified segmented navigation separating game engines into isolated views.
- Rock-Paper-Scissors scoring engine with first-to-5 victory arbitration.
- Two-player 3x3 Tic-Tac-Toe state machine with automated win/stalemate detection.
- Decoupled state reset routines allowing instant game restarts.

## Prerequisites

- Python 3.10 or higher
- Required packages:

```bash
pip install customtkinter
```

## Execution

Initialize and run the module via the command line:

```bash
python "games.py"
```

## Project Structure

```
.
â”œâ”€â”€ games.py
â”œâ”€â”€ LICENSE             # MIT License
â””â”€â”€ README.md           # Developer documentation
```

## License

This project is licensed under the terms of the MIT License. Refer to the `LICENSE` file for details.

---

### 🌐 Connect with Me

<p align="left">
  <a href="http://xrefs0.com/" target="_blank">
    <img src="https://img.icons8.com/bubbles/60/000000/domain.png" title="Website" width="45" height="45"/>
  </a>
  <a href="https://www.facebook.com/XREFS0" target="_blank">
    <img src="https://img.icons8.com/bubbles/60/000000/facebook-new.png" title="Facebook Page" width="45" height="45"/>
  </a>
  <a href="https://t.me/MrMasaOfficial" target="_blank">
    <img src="https://img.icons8.com/bubbles/60/000000/telegram-app.png" title="Telegram Contact" width="45" height="45"/>
  </a>
  <a href="https://t.me/XREFS0_CHANNEL" target="_blank">
    <img src="https://img.icons8.com/bubbles/60/000000/telegram-app.png" title="Telegram Channel" width="45" height="45"/>
  </a>
  <a href="https://www.youtube.com/@XREFS0" target="_blank">
    <img src="https://img.icons8.com/bubbles/60/000000/youtube-play.png" title="YouTube" width="45" height="45"/>
  </a>
</p>


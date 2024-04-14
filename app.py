from textual.app import App, ComposeResult 
from textual.screen import Screen
from textual.containers import Container , Center, ScrollableContainer
from textual.widgets import Header, Footer , Button , Static, Label , Input , Digits, DataTable
import art

ROWS = [
    ("lane", "swimmer", "country", "time"),
    (4, "Joseph Schooling", "Singapore", 50.39),
    (2, "Michael Phelps", "United States", 51.14),
    (5, "Chad le Clos", "South Africa", 51.14),
    (6, "László Cseh", "Hungary", 51.14),
    (3, "Li Zhuhao", "China", 51.26),
    (8, "Mehdy Metella", "France", 51.58),
    (7, "Tom Shields", "United States", 51.73),
    (1, "Aleksandr Sadovnikov", "Russia", 51.84),
    (10, "Darren Burns", "Scotland", 51.84),
]


class ResultScreen(Screen):
    "The analytics screen"
    CSS_PATH="ResultScreen.tcss"
    BINDINGS = [("d", "toggle_dark", "Toggle dark mode") ,("escape", "app.pop_screen('resultscreen')", "Pop Screen")]



    def compose(self) -> ComposeResult:
        """Create child widgets for the analytics screen."""
        yield Header()
        with Center():
            yield Label("your score is : 90" , id="score")
        with Center():
            yield Label("Stats:" , id="statsTitle")
        
        yield Container(            
            ScrollableContainer(
                DataTable( id="table"),
                id="tableScrollContainer"
            ),
            Center(
            Label("Your wpm is: 90" , id="wmp"),
            id="wpmContainer")
            , id="statsContainer"
        )

    def on_mount(self) -> None:
        table = self.query_one(DataTable)
        table.add_columns(*ROWS[0])
        table.add_rows(ROWS[1:])




class GameScreen(Screen):
    "The Gameplay screen"
    CSS_PATH="GameScreen.tcss"
    BINDINGS = [("escape", "app.pop_screen('gamescreen')", "Back To Main Menu") ,("d", "toggle_dark", "Toggle Dark Mode") ]

    def compose(self) -> ComposeResult:
        """Create child widgets for the game screen."""
        yield Header()
        yield Digits("100000" , id="timer")
        yield Container(
            Label("Type this:" , id="Instruction"),
            Label("word" , id="gameWord"),
            Container( Input(placeholder="type here...", id="userInput"), classes="inputContainer" ),
            classes="containerGame"
        ) 
        yield Footer()


class TypingCoach(App):
    """An app to help you typer faster."""
    CSS_PATH="MainScreen.tcss"
    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]
    
    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Event handler called when start button is pressed."""
        if event.button.id == "gameStartButton":
            self.push_screen(GameScreen())


    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        with Container(id="mainContainer"):
            with Center():
                yield Label(art.text2art("TypingCoach" , font="doom") , id="mainTitle")
            with Center():
                yield Label("A game that will me you type faster using the power of python and data analytics" , id="description")
            with Center():
                yield Button("Start" , id="gameStartButton" , variant="success")
        yield Footer()

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.dark = not self.dark


if __name__ == "__main__":
    app = TypingCoach()
    app.run()

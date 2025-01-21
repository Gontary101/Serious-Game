import tkinter as tk
from tkinter import ttk, messagebox
from dataclasses import dataclass, field
from typing import List, Dict, Optional
import json

# ---------------------- Predefined Game Data (JSON) ----------------------

FACTORIES_JSON = """
[
    {
        "name": "Timber Logging Camp",
        "construction_cost": 150,
        "operational_cost": 20,
        "pollution": 3,
        "output": {"Wood": 2},
        "resource_requirements": {},
        "allowed_terrain": ["Forest"],
        "workers_required": {"Technician": 1},
        "transportation_needed": [],
        "ec_output": 100
    },
    {
        "name": "Crop Farm",
        "construction_cost": 200,
        "operational_cost": 25,
        "pollution": 2,
        "output": {"Water": 3},
        "resource_requirements": {},
        "allowed_terrain": ["Plains", "Coastal"],
        "workers_required": {"Universal Worker": 1},
        "transportation_needed": [],
        "ec_output": 120
    },
    {
        "name": "Mine & Smelter",
        "construction_cost": 300,
        "operational_cost": 40,
        "pollution": 8,
        "output": {"Minerals": 2},
        "resource_requirements": {},
        "allowed_terrain": ["Mountain"],
        "workers_required": {"Technician": 1},
        "transportation_needed": ["Minerals"],
        "ec_output": 200
    },
    {
        "name": "Bioplastics Plant",
        "construction_cost": 250,
        "operational_cost": 30,
        "pollution": 5,
        "output": {"Plastics": 2},
        "resource_requirements": {"Wood": 1, "Water": 1},
        "allowed_terrain": ["Urban", "Plains", "Forest"],
        "workers_required": {"Environmental Advisor": 1},
        "transportation_needed": ["Wood", "Water"],
        "ec_output": 180
    },
    {
        "name": "Solar Panel Assembly",
        "construction_cost": 300,
        "operational_cost": 25,
        "pollution": 3,
        "output": {"Solar Panel": 2},
        "resource_requirements": {},
        "allowed_terrain": ["Urban", "Plains"],
        "workers_required": {"Engineer": 1},
        "transportation_needed": [],
        "ec_output": 220
    },
    {
        "name": "Wind Turbine Factory",
        "construction_cost": 350,
        "operational_cost": 30,
        "pollution": 4,
        "output": {"Wind Turbine": 1},
        "resource_requirements": {},
        "allowed_terrain": ["Urban", "Plains"],
        "workers_required": {"Engineer": 1, "Technician": 1},
        "transportation_needed": [],
        "ec_output": 250
    },
    {
        "name": "Recycling Center",
        "construction_cost": 200,
        "operational_cost": 20,
        "pollution": 4,
        "output": {"Recycled Materials": 1},
        "resource_requirements": {"Plastics": 1},
        "allowed_terrain": ["Urban"],
        "workers_required": {"Technician": 1},
        "transportation_needed": ["Plastics"],
        "ec_output": 150
    },
    {
        "name": "Urban Manufacturing Plant",
        "construction_cost": 300,
        "operational_cost": 35,
        "pollution": 6,
        "output": {"Manufactured Goods": 2},
        "resource_requirements": {"Minerals": 2, "Recycled Materials": 2},
        "allowed_terrain": ["Urban"],
        "workers_required": {"Engineer": 1, "Technician": 1},
        "transportation_needed": ["Minerals", "Recycled Materials"],
        "ec_output": 300
    },
    {
        "name": "Sustainable Fishery",
        "construction_cost": 250,
        "operational_cost": 20,
        "pollution": 2,
        "output": {"Fish": 2},
        "resource_requirements": {"Water": 1},
        "allowed_terrain": ["Coastal"],
        "workers_required": {"Universal Worker": 1},
        "transportation_needed": ["Water"],
        "ec_output": 140
    },
    {
        "name": "Eco-Consulting Agency",
        "construction_cost": 150,
        "operational_cost": 15,
        "pollution": 1,
        "output": {"Consultancy Services": 20},
        "resource_requirements": {},
        "allowed_terrain": ["Urban"],
        "workers_required": {"Environmental Advisor": 1},
        "transportation_needed": [],
        "ec_output": 250
    }
]
"""

TECHNOLOGIES_JSON = """
[
    {
        "name": "Solar-Wind Hybrid Array",
        "category": "Renewable Energy",
        "cost": 250,
        "maintenance": 20,
        "effect": "Reduces a single factory’s operational cost by 10 and pollution by 3.",
        "prerequisites": []
    },
    {
        "name": "Advanced Automation Module",
        "category": "Process Optimization",
        "cost": 200,
        "maintenance": 15,
        "effect": "+20% production in that factory.",
        "prerequisites": ["Engineer"]
    },
    {
        "name": "Carbon Capture System",
        "category": "Pollution Control",
        "cost": 250,
        "maintenance": 20,
        "effect": "-6 pollution from the assigned factory each round.",
        "prerequisites": ["Environmental Advisor"]
    },
    {
        "name": "Bioplastic Synthesis Upgrade",
        "category": "Green Chemistry",
        "cost": 200,
        "maintenance": 10,
        "effect": "+10 EC per Bioplastics unit sold.",
        "prerequisites": []
    },
    {
        "name": "Industrial Recycling Unit",
        "category": "Waste Management",
        "cost": 200,
        "maintenance": 15,
        "effect": "Converts factory waste into Recycled Materials.",
        "prerequisites": ["Technician"]
    },
    {
        "name": "Closed-Loop Water System",
        "category": "Pollution Control",
        "cost": 150,
        "maintenance": 10,
        "effect": "-2 pollution from water pollution, saves 5 EC/round.",
        "prerequisites": ["Environmental Advisor"]
    },
    {
        "name": "Vertical Integration Logistics",
        "category": "Logistics",
        "cost": 300,
        "maintenance": 20,
        "effect": "Run up to 2 factories on the same tile. +5 EC/round in transport savings.",
        "prerequisites": []
    },
    {
        "name": "Urban Rooftop Farming",
        "category": "Agriculture / Urban",
        "cost": 100,
        "maintenance": 5,
        "effect": "+2 units of fresh produce with minimal pollution (+1 PP).",
        "prerequisites": []
    },
    {
        "name": "Electric Transport Network",
        "category": "Transportation",
        "cost": 200,
        "maintenance": 10,
        "effect": "Reduce transportation pollution by 50% for Electric Transport routes.",
        "prerequisites": []
    },
    {
        "name": "Fossil Fuel Subsidy",
        "category": "Economic Policy",
        "cost": 150,
        "maintenance": 5,
        "effect": "Reduce Fossil Fuel transportation costs by 10 EC per distance unit.",
        "prerequisites": []
    }
]
"""

TRANSPORTATION_JSON = """
[
    {
        "type": "Electric",
        "cost_per_distance": 50,
        "pollution_per_distance": 1
    },
    {
        "type": "Fossil Fuel",
        "cost_per_distance": 30,
        "pollution_per_distance": 3
    }
]
"""

# ---------------------- Data Classes ----------------------

@dataclass
class Technology:
    name: str
    category: str
    cost: int
    maintenance: int
    effect: str
    prerequisites: List[str] = field(default_factory=list)

@dataclass
class Worker:
    role: str  # Engineer, Technician, Environmental Advisor, Universal Worker
    salary: int
    benefit: str

@dataclass
class Factory:
    name: str
    construction_cost: int
    operational_cost: int
    pollution: int
    output: Dict[str, int]
    resource_requirements: Dict[str, int]
    allowed_terrain: List[str]
    workers_required: Dict[str, int]
    transportation_needed: List[str]
    transportation: Dict[str, Dict[str, int]] = field(default_factory=dict)
    workers_assigned: Dict[str, int] = field(default_factory=dict)
    upgrades: List[str] = field(default_factory=list)
    ec_output: int = 0  # direct money output from the factory each round

@dataclass
class Player:
    name: str
    ec: int = 1500
    pp: int = 0
    factories: List[Factory] = field(default_factory=list)
    technologies: List[Technology] = field(default_factory=list)
    workers: List[Worker] = field(default_factory=list)
    carbon_credits: int = 0
    resources: Dict[str, int] = field(default_factory=lambda: {
        'Minerals': 0,
        'Wood': 0,
        'Oil': 0,
        'Water': 0,
        'Plastics': 0,
        'Bioplastics': 0,
        'Solar Panel': 0,
        'Wind Turbine': 0,
        'Recycled Materials': 0,
        'Manufactured Goods': 0,
        'Fish': 0,
        'Consultancy Services': 0
    })

@dataclass
class TerrainTile:
    terrain_type: str
    purchase_cost: int
    resources: List[str]
    carbon_offset: int
    owned_by: Optional[str] = None

# ---------------------- Game State ----------------------

class GameState:
    def __init__(self):
        self.players: List[Player] = []
        self.terrain_tiles: List[TerrainTile] = self.initialize_terrain()
        self.current_round: int = 1
        self.max_rounds: int = 6
        self.transportation_types: List[Dict] = self.load_transportation()
        self.factories_data: List[Dict] = self.load_factories()
        self.technologies_data: List[Dict] = self.load_technologies()

    def load_factories(self) -> List[Dict]:
        return json.loads(FACTORIES_JSON)

    def load_technologies(self) -> List[Dict]:
        return json.loads(TECHNOLOGIES_JSON)

    def load_transportation(self) -> List[Dict]:
        return json.loads(TRANSPORTATION_JSON)

    def initialize_terrain(self) -> List[TerrainTile]:
        # Example initialization; in a real game, this might be randomized
        return [
            TerrainTile("Plains", 200, ["Wood", "Water"], 5),
            TerrainTile("Forest", 250, ["Wood"], 10),
            TerrainTile("Mountain", 300, ["Minerals", "Oil"], 3),
            TerrainTile("Coastal", 250, ["Water", "Oil"], 7),
            TerrainTile("Urban", 350, ["Plastics", "Water"], 2),
            TerrainTile("Plains", 200, ["Wood", "Water"], 5),
            TerrainTile("Forest", 250, ["Wood"], 10),
            TerrainTile("Mountain", 300, ["Minerals", "Oil"], 3),
            TerrainTile("Coastal", 250, ["Water", "Oil"], 7),
            TerrainTile("Urban", 350, ["Plastics", "Water"], 2),
            TerrainTile("Plains", 200, ["Wood", "Water"], 5),
            TerrainTile("Forest", 250, ["Wood"], 10),
            TerrainTile("Mountain", 300, ["Minerals", "Oil"], 3),
            TerrainTile("Coastal", 250, ["Water", "Oil"], 7),
            TerrainTile("Urban", 350, ["Plastics", "Water"], 2),
            TerrainTile("Plains", 200, ["Wood", "Water"], 5),
            TerrainTile("Forest", 250, ["Wood"], 10),
            TerrainTile("Mountain", 300, ["Minerals", "Oil"], 3),
            TerrainTile("Coastal", 250, ["Water", "Oil"], 7),
            TerrainTile("Urban", 350, ["Plastics", "Water"], 2),
        ]

    def add_player(self, player_name: str):
        if len(self.players) >= 4:
            raise Exception("Maximum of 4 players reached.")
        self.players.append(Player(name=player_name))

# ---------------------- Companion App GUI ----------------------

class CompanionApp(tk.Tk):
    def __init__(self, game_state: GameState):
        super().__init__()
        self.title("Enhanced ECO-FACTORY CHALLENGE Companion App")
        self.geometry("1600x900")
        
        self.configure(bg="#F0F4F7")

        style = ttk.Style(self)
        style.theme_use("clam")
        style.configure("TFrame", background="#F0F4F7")
        style.configure("TLabel", background="#F0F4F7", font=("Arial", 10, "bold"), foreground="#2B2B2B")
        style.configure("TButton",
                        font=("Arial", 10, "bold"),
                        foreground="#FFFFFF",
                        background="#6699CC",
                        padding=6)
        style.configure("TNotebook", background="#F0F4F7")
        style.configure("TNotebook.Tab", background="#BED7F3", foreground="#000000", padding=(10, 5))
        style.configure("Treeview",
                        background="#FFFFFF",
                        foreground="#2B2B2B",
                        rowheight=25,
                        fieldbackground="#FFFFFF")
        style.map("Treeview",
                  background=[("selected", "#5B9BD5")],
                  foreground=[("selected", "#FFFFFF")])
        style.configure("Vertical.TScrollbar", background="#BED7F3")

        self.game_state = game_state
        self.selected_player: Optional[Player] = None

        # Load predefined data
        self.factories_list = self.load_factories()
        self.technologies_list = self.load_technologies()
        self.transportation_types = self.game_state.transportation_types

        # Create all widgets
        self.create_widgets()

    def load_factories(self) -> List[Factory]:
        factories = []
        for f in self.game_state.factories_data:
            factory = Factory(
                name=f["name"],
                construction_cost=f["construction_cost"],
                operational_cost=f["operational_cost"],
                pollution=f["pollution"],
                output=f["output"],
                resource_requirements=f["resource_requirements"],
                allowed_terrain=f["allowed_terrain"],
                workers_required=f["workers_required"],
                transportation_needed=f["transportation_needed"],
                ec_output=f.get("ec_output", 0)
            )
            factories.append(factory)
        return factories

    def load_technologies(self) -> List[Technology]:
        technologies = []
        for t in self.game_state.technologies_data:
            tech = Technology(
                name=t["name"],
                category=t["category"],
                cost=t["cost"],
                maintenance=t["maintenance"],
                effect=t["effect"],
                prerequisites=t["prerequisites"]
            )
            technologies.append(tech)
        return technologies

    def create_widgets(self):
        # Player Selection Frame
        player_frame = ttk.Frame(self)
        player_frame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)

        ttk.Label(player_frame, text="Select Player:").pack(side=tk.LEFT)

        self.player_var = tk.StringVar()
        self.player_dropdown = ttk.Combobox(player_frame, textvariable=self.player_var, state="readonly")
        self.player_dropdown['values'] = [player.name for player in self.game_state.players]
        self.player_dropdown.bind("<<ComboboxSelected>>", self.update_selected_player)
        self.player_dropdown.pack(side=tk.LEFT, padx=5)

        ttk.Button(player_frame, text="Add Player", command=self.add_player_dialog).pack(side=tk.LEFT, padx=5)

        # Notebook for Tabs
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(expand=1, fill='both', padx=10, pady=10)

        # Dashboard Tab
        self.dashboard_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.dashboard_tab, text='Dashboard')
        self.create_dashboard_tab()

        # Terrain Tab
        self.terrain_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.terrain_tab, text='Terrain')
        self.create_terrain_tab()

        # Factories Tab
        self.factories_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.factories_tab, text='Factories')
        self.create_factories_tab()

        # Technologies Tab
        self.technologies_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.technologies_tab, text='Technologies')
        self.create_technologies_tab()

        # Workers Tab
        self.workers_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.workers_tab, text='Workers')
        self.create_workers_tab()

        # Resources Tab
        self.resources_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.resources_tab, text='Resources')
        self.create_resources_tab()

        # Pollution & Costs Tab
        self.pollution_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.pollution_tab, text='Pollution & Costs')
        self.create_pollution_tab()

    # ---------------------- Player Management ----------------------

    def add_player_dialog(self):
        def add_player():
            name = entry.get().strip()
            if name == "":
                messagebox.showerror("Error", "Player name cannot be empty.")
                return
            if name in [player.name for player in self.game_state.players]:
                messagebox.showerror("Error", "Player name already exists.")
                return
            try:
                self.game_state.add_player(name)
                self.player_dropdown['values'] = [player.name for player in self.game_state.players]
                add_window.destroy()
                messagebox.showinfo("Success", f"Player '{name}' added successfully.")
            except Exception as e:
                messagebox.showerror("Error", str(e))

        add_window = tk.Toplevel(self)
        add_window.title("Add Player")
        add_window.geometry("300x150")
        add_window.configure(bg="#F0F4F7")

        ttk.Label(add_window, text="Player Name:").pack(padx=10, pady=10)
        entry = ttk.Entry(add_window)
        entry.pack(padx=10, pady=5)

        ttk.Button(add_window, text="Add", command=add_player).pack(padx=10, pady=10)

    def update_selected_player(self, event):
        player_name = self.player_var.get()
        self.selected_player = next((p for p in self.game_state.players if p.name == player_name), None)
        self.refresh_tabs()

    # ---------------------- Tabs Creation ----------------------

    def create_dashboard_tab(self):
        self.dashboard_info = ttk.Label(
            self.dashboard_tab,
            text="Select a player to view dashboard.",
            justify=tk.LEFT,
            font=("Arial", 14, "bold"),
            foreground="#333333"
        )
        self.dashboard_info.pack(anchor=tk.W, padx=20, pady=20)

    def create_terrain_tab(self):
        frame = ttk.Frame(self.terrain_tab)
        frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.terrain_tree = ttk.Treeview(
            frame,
            columns=("ID", "Terrain Type", "Purchase Cost", "Resources", "Carbon Offset", "Owned By"),
            show='headings'
        )
        for col in ("ID", "Terrain Type", "Purchase Cost", "Resources", "Carbon Offset", "Owned By"):
            self.terrain_tree.heading(col, text=col)
            self.terrain_tree.column(col, width=150, anchor=tk.CENTER)
        self.terrain_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=self.terrain_tree.yview)
        self.terrain_tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=tk.LEFT, fill=tk.Y)

        btn_frame = ttk.Frame(frame)
        btn_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10)

        ttk.Button(btn_frame, text="Purchase Terrain", command=self.purchase_terrain_dialog).pack(pady=5)
        ttk.Button(btn_frame, text="Refresh Terrain", command=self.refresh_terrain).pack(pady=5)

        self.refresh_terrain()

    def create_factories_tab(self):
        frame = ttk.Frame(self.factories_tab)
        frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.factory_tree = ttk.Treeview(
            frame,
            columns=("Name", "Construction Cost", "Operational Cost", "Pollution", "Output",
                     "Resources", "Transportation", "Workers", "EC Output"),
            show='headings'
        )
        for col in ("Name", "Construction Cost", "Operational Cost", "Pollution", "Output",
                    "Resources", "Transportation", "Workers", "EC Output"):
            self.factory_tree.heading(col, text=col)
            self.factory_tree.column(col, width=120, anchor=tk.CENTER)
        self.factory_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=self.factory_tree.yview)
        self.factory_tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=tk.LEFT, fill=tk.Y)

        btn_frame = ttk.Frame(frame)
        btn_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10)

        ttk.Button(btn_frame, text="Add Factory", command=self.add_factory_dialog).pack(pady=5)
        ttk.Button(btn_frame, text="Remove Factory", command=self.remove_factory).pack(pady=5)
        ttk.Button(btn_frame, text="Refresh Factories", command=self.refresh_factories).pack(pady=5)

    def create_technologies_tab(self):
        frame = ttk.Frame(self.technologies_tab)
        frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.tech_tree = ttk.Treeview(
            frame,
            columns=("Name", "Category", "Cost", "Maintenance", "Effect", "Prerequisites"),
            show='headings'
        )
        for col in ("Name", "Category", "Cost", "Maintenance", "Effect", "Prerequisites"):
            self.tech_tree.heading(col, text=col)
            self.tech_tree.column(col, width=150, anchor=tk.CENTER)
        self.tech_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=self.tech_tree.yview)
        self.tech_tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=tk.LEFT, fill=tk.Y)

        btn_frame = ttk.Frame(frame)
        btn_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10)

        ttk.Button(btn_frame, text="Purchase Technology", command=self.purchase_technology_dialog).pack(pady=5)
        ttk.Button(btn_frame, text="Remove Technology", command=self.remove_technology).pack(pady=5)
        ttk.Button(btn_frame, text="Refresh Technologies", command=self.refresh_technologies).pack(pady=5)

    def create_workers_tab(self):
        frame = ttk.Frame(self.workers_tab)
        frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.worker_tree = ttk.Treeview(
            frame,
            columns=("Role", "Salary", "Benefit"),
            show='headings'
        )
        for col in ("Role", "Salary", "Benefit"):
            self.worker_tree.heading(col, text=col)
            self.worker_tree.column(col, width=200, anchor=tk.CENTER)
        self.worker_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=self.worker_tree.yview)
        self.worker_tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=tk.LEFT, fill=tk.Y)

        btn_frame = ttk.Frame(frame)
        btn_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10)

        ttk.Button(btn_frame, text="Hire Worker", command=self.hire_worker_dialog).pack(pady=5)
        ttk.Button(btn_frame, text="Assign Worker", command=self.assign_worker_dialog).pack(pady=5)
        ttk.Button(btn_frame, text="Remove Worker", command=self.remove_worker).pack(pady=5)
        ttk.Button(btn_frame, text="Refresh Workers", command=self.refresh_workers).pack(pady=5)

    def create_resources_tab(self):
        frame = ttk.Frame(self.resources_tab)
        frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.resource_tree = ttk.Treeview(
            frame,
            columns=("Resource", "Produced", "Consumed", "Traded", "Inventory"),
            show='headings'
        )
        for col in ("Resource", "Produced", "Consumed", "Traded", "Inventory"):
            self.resource_tree.heading(col, text=col)
            self.resource_tree.column(col, width=120, anchor=tk.CENTER)
        self.resource_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=self.resource_tree.yview)
        self.resource_tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=tk.LEFT, fill=tk.Y)

        btn_frame = ttk.Frame(frame)
        btn_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10)

        ttk.Button(btn_frame, text="Trade Resources", command=self.trade_resources_dialog).pack(pady=5)
        ttk.Button(btn_frame, text="Sell Resources", command=self.sell_resources_dialog).pack(pady=5)
        ttk.Button(btn_frame, text="Refresh Resources", command=self.refresh_resources).pack(pady=5)

        self.refresh_resources()

    def create_pollution_tab(self):
        frame = ttk.Frame(self.pollution_tab)
        frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.pollution_info = ttk.Label(
            frame,
            text="Select a player to view pollution and costs.",
            justify=tk.LEFT,
            font=("Arial", 14, "bold"),
            foreground="#333333"
        )
        self.pollution_info.pack(anchor=tk.W, padx=20, pady=20)

        ttk.Button(frame, text="Calculate Round", command=self.calculate_round).pack(pady=10)

    # ---------------------- Refresh Methods ----------------------

    def refresh_tabs(self):
        self.refresh_dashboard()
        self.refresh_terrain()
        self.refresh_factories()
        self.refresh_technologies()
        self.refresh_workers()
        self.refresh_resources()
        self.refresh_pollution()

    def refresh_dashboard(self):
        if not self.selected_player:
            self.dashboard_info.config(text="Select a player to view dashboard.")
            return
        info = (
            f"Player: {self.selected_player.name}\n"
            f"Eco-Credits (EC): {self.selected_player.ec}\n"
            f"Pollution Points (PP): {self.selected_player.pp}\n"
            f"Carbon Credits: {self.selected_player.carbon_credits}"
        )
        self.dashboard_info.config(text=info)

    def refresh_terrain(self):
        for item in self.terrain_tree.get_children():
            self.terrain_tree.delete(item)
        for idx, tile in enumerate(self.game_state.terrain_tiles):
            owned_by = tile.owned_by if tile.owned_by else "None"
            resources_str = ", ".join(tile.resources)
            self.terrain_tree.insert("", tk.END, values=(
                idx + 1,
                tile.terrain_type,
                tile.purchase_cost,
                resources_str,
                tile.carbon_offset,
                owned_by
            ))

    def refresh_factories(self):
        for item in self.factory_tree.get_children():
            self.factory_tree.delete(item)
        if not self.selected_player:
            return
        for factory in self.selected_player.factories:
            output_str = ", ".join(f"{k}: {v}" for k, v in factory.output.items())
            resources_str = "None"
            if factory.resource_requirements:
                resources_str = ", ".join(f"{k}: {v}" for k, v in factory.resource_requirements.items())
            transportation = "N/A"
            if factory.transportation:
                transportation = ", ".join(
                    f"{res}: {trans['type']} ({trans['distance']})"
                    for res, trans in factory.transportation.items()
                )
            workers = "None"
            if factory.workers_assigned:
                workers = ", ".join(f"{role}: {count}" for role, count in factory.workers_assigned.items())

            self.factory_tree.insert("", tk.END, values=(
                factory.name,
                factory.construction_cost,
                factory.operational_cost,
                factory.pollution,
                output_str,
                resources_str,
                transportation,
                workers,
                factory.ec_output
            ))

    def refresh_technologies(self):
        for item in self.tech_tree.get_children():
            self.tech_tree.delete(item)
        if not self.selected_player:
            return
        for tech in self.selected_player.technologies:
            prereq = ", ".join(tech.prerequisites) if tech.prerequisites else "None"
            self.tech_tree.insert("", tk.END, values=(
                tech.name,
                tech.category,
                tech.cost,
                tech.maintenance,
                tech.effect,
                prereq
            ))

    def refresh_workers(self):
        for item in self.worker_tree.get_children():
            self.worker_tree.delete(item)
        if not self.selected_player:
            return
        for worker in self.selected_player.workers:
            self.worker_tree.insert("", tk.END, values=(
                worker.role,
                worker.salary,
                worker.benefit
            ))

    def refresh_resources(self):
        for item in self.resource_tree.get_children():
            self.resource_tree.delete(item)
        if not self.selected_player:
            return
        resource_summary = {
            r: {'Produced': 0, 'Consumed': 0, 'Traded': 0, 'Inventory': self.selected_player.resources[r]}
            for r in self.selected_player.resources
        }
        for factory in self.selected_player.factories:
            for res, qty in factory.output.items():
                if res != "Consultancy Services":  # Consultancy Services are treated as EC
                    resource_summary[res]['Produced'] += qty
            for res, qty in factory.resource_requirements.items():
                if res in resource_summary:
                    resource_summary[res]['Consumed'] += qty
        for res, data in resource_summary.items():
            self.resource_tree.insert("", tk.END, values=(
                res,
                data['Produced'],
                data['Consumed'],
                data['Traded'],
                data['Inventory']
            ))

    def refresh_pollution(self):
        if not self.selected_player:
            self.pollution_info.config(text="Select a player to view pollution and costs.")
            return
        total_pollution = self.calculate_total_pollution_for_player(self.selected_player)
        carbon_tax = 5 * total_pollution
        total_salary = sum(worker.salary for worker in self.selected_player.workers)
        total_maintenance = sum(tech.maintenance for tech in self.selected_player.technologies)
        transportation_cost = 0
        for factory in self.selected_player.factories:
            for trans in factory.transportation.values():
                trans_type = trans['type']
                distance = trans['distance']
                transport_info = next((t for t in self.transportation_types if t['type'] == trans_type), None)
                if transport_info:
                    cost = transport_info['cost_per_distance'] * distance
                    for tech in self.selected_player.technologies:
                        if "Reduce Fossil Fuel transportation costs by 10 EC per distance unit." in tech.effect and trans_type == "Fossil Fuel":
                            cost = max(cost - 10 * distance, 0)
                    transportation_cost += cost

        info = (
            f"Total Pollution Points (PP): {total_pollution}\n"
            f"Carbon Tax (5 EC × PP): {carbon_tax} EC\n"
            f"Total Worker Salaries: {total_salary} EC\n"
            f"Total Technology Maintenance: {total_maintenance} EC\n"
            f"Total Transportation Cost: {transportation_cost} EC"
        )
        self.pollution_info.config(text=info)

    # ---------------------- Round Calculation ----------------------

    def calculate_round(self):
        if not self.game_state.players:
            messagebox.showerror("Error", "No players in the game.")
            return

        round_summary = ""
        game_end = False
        winner = None

        for player in self.game_state.players:
            total_pollution = self.calculate_total_pollution_for_player(player)
            carbon_tax = 5 * total_pollution

            total_salary = sum(worker.salary for worker in player.workers)
            total_maintenance = sum(tech.maintenance for tech in player.technologies)

            transportation_cost = 0
            for factory in player.factories:
                for trans in factory.transportation.values():
                    trans_type = trans['type']
                    distance = trans['distance']
                    transport_info = next((t for t in self.transportation_types if t['type'] == trans_type), None)
                    if transport_info:
                        cost = transport_info['cost_per_distance'] * distance
                        for tech in player.technologies:
                            if "Reduce Fossil Fuel transportation costs by 10 EC per distance unit." in tech.effect and trans_type == "Fossil Fuel":
                                cost = max(cost - 10 * distance, 0)
                        transportation_cost += cost

            # Resource-based revenue and resource production:
            # First, handle direct factory EC output
            factory_direct_ec = sum(f.ec_output for f in player.factories)

            production_revenue = 0
            # Now factories consume required resources and produce outputs
            for factory in player.factories:
                # Check if we have enough resources to run this factory
                can_produce = True
                for r_need, q_need in factory.resource_requirements.items():
                    if player.resources.get(r_need, 0) < q_need:
                        can_produce = False
                        break

                if can_produce:
                    # Subtract the required resources
                    for r_need, q_need in factory.resource_requirements.items():
                        player.resources[r_need] -= q_need

                    # Produce the factory's outputs
                    for r_out, q_out in factory.output.items():
                        if r_out == "Consultancy Services":
                            # Consultancy Services count as direct EC
                            production_revenue += q_out
                        else:
                            # Add produced resource to player's inventory
                            player.resources[r_out] += q_out
                            # Also add revenue for these produced goods
                            production_revenue += q_out * 50

            total_production_revenue = factory_direct_ec + production_revenue

            total_expenses = carbon_tax + total_salary + total_maintenance + transportation_cost

            # Add production revenue first
            player.ec += total_production_revenue

            # Then subtract expenses
            if player.ec < total_expenses:
                round_summary += f"{player.name} has insufficient Eco-Credits to cover expenses this round.\n"
                continue

            player.ec -= total_expenses
            player.pp = total_pollution

            net_change = total_production_revenue - total_expenses
            round_summary += (
                f"{player.name}:\n"
                f"  Production Revenue: {total_production_revenue} EC\n"
                f"  Expenses: {total_expenses} EC\n"
                f"  Net Change: {net_change} EC\n"
                f"  Current EC: {player.ec} EC\n"
                f"  Current PP: {player.pp} PP\n\n"
            )

            if player.ec >= 3000:
                winner = player
                game_end = True
                break

        self.refresh_tabs()

        if game_end:
            round_summary += f"{winner.name} has reached 3000 EC! The game ends now.\n"
            self.end_game()
        else:
            round_summary += f"Round {self.game_state.current_round} completed.\n"
            self.game_state.current_round += 1
            if self.game_state.current_round > self.game_state.max_rounds:
                self.end_game()

        messagebox.showinfo("Round Calculated", round_summary)

    def calculate_total_pollution_for_player(self, player: Player) -> int:
        total_pollution = 0
        for factory in player.factories:
            total_pollution += factory.pollution
            for trans in factory.transportation.values():
                trans_type = trans['type']
                distance = trans['distance']
                transport_info = next((t for t in self.transportation_types if t['type'] == trans_type), None)
                if transport_info:
                    pollution = transport_info['pollution_per_distance'] * distance
                    # Apply technology effects
                    for tech in player.technologies:
                        if "Reduce transportation pollution by 50%" in tech.effect and trans_type == "Electric":
                            pollution = pollution // 2
                    total_pollution += pollution

        # Tech-based pollution reductions
        for tech in player.technologies:
            if "pollution" in tech.effect.lower():
                import re
                reductions = map(int, re.findall(r'-\d+', tech.effect))
                for reduction in reductions:
                    total_pollution += reduction  # reduction is negative

        # Worker-based pollution reductions
        for worker in player.workers:
            if worker.role == "Environmental Advisor":
                total_pollution -= 3

        return max(total_pollution, 0)

    # ---------------------- Worker Management ----------------------

    def hire_worker_dialog(self):
        if not self.selected_player:
            messagebox.showerror("Error", "No player selected.")
            return

        add_window = tk.Toplevel(self)
        add_window.title("Hire Worker")
        add_window.geometry("400x300")
        add_window.configure(bg="#F0F4F7")

        ttk.Label(add_window, text="Select Worker Role:").grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
        worker_role_var = tk.StringVar()
        worker_roles = ["Engineer", "Technician", "Environmental Advisor", "Universal Worker"]
        worker_dropdown = ttk.Combobox(add_window, textvariable=worker_role_var, state="readonly")
        worker_dropdown['values'] = worker_roles
        worker_dropdown.current(0)
        worker_dropdown.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)

        worker_details = tk.Text(add_window, width=40, height=5, wrap='word', state='disabled')
        worker_details.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

        def display_worker_details(event):
            role = worker_role_var.get()
            info = {
                "Engineer": {"salary": 50, "benefit": "+20% production in advanced factories, or +10% in basic factories."},
                "Technician": {"salary": 30, "benefit": "Maintains baseline production. Required for certain factories."},
                "Environmental Advisor": {"salary": 40, "benefit": "-3 pollution in the factory they’re assigned to."},
                "Universal Worker": {"salary": 20, "benefit": "Minimal production help; no special pollution or efficiency bonuses."}
            }
            if role in info:
                details = (
                    f"Role: {role}\n"
                    f"Salary: {info[role]['salary']} EC/round\n"
                    f"Benefit: {info[role]['benefit']}"
                )
                worker_details.config(state='normal')
                worker_details.delete(1.0, tk.END)
                worker_details.insert(tk.END, details)
                worker_details.config(state='disabled')

        worker_dropdown.bind("<<ComboboxSelected>>", display_worker_details)
        display_worker_details(None)  # Display details for the default selection

        def hire_worker():
            role = worker_role_var.get()
            info = {
                "Engineer": {"salary": 50, "benefit": "+20% production in advanced factories, or +10% in basic factories."},
                "Technician": {"salary": 30, "benefit": "Maintains baseline production. Required for certain factories."},
                "Environmental Advisor": {"salary": 40, "benefit": "-3 pollution in the factory they’re assigned to."},
                "Universal Worker": {"salary": 20, "benefit": "Minimal production help; no special pollution or efficiency bonuses."}
            }
            if role not in info:
                messagebox.showerror("Error", "Invalid worker role selected.")
                return
            salary = info[role]["salary"]
            if self.selected_player.ec < salary:
                messagebox.showerror("Error", "Not enough EC to hire this worker.")
                return
            self.selected_player.ec -= salary
            w = Worker(role=role, salary=salary, benefit=info[role]["benefit"])
            self.selected_player.workers.append(w)
            add_window.destroy()
            self.refresh_workers()
            self.refresh_dashboard()
            messagebox.showinfo("Success", f"{role} hired successfully.")

        ttk.Button(add_window, text="Hire", command=hire_worker).grid(row=2, column=0, columnspan=2, pady=20)

    def assign_worker_dialog(self):
        if not self.selected_player:
            messagebox.showerror("Error", "No player selected.")
            return
        if not self.selected_player.workers:
            messagebox.showerror("Error", "No workers available to assign.")
            return
        if not self.selected_player.factories:
            messagebox.showerror("Error", "No factories available to assign workers.")
            return

        assign_window = tk.Toplevel(self)
        assign_window.title("Assign Worker")
        assign_window.geometry("500x300")
        assign_window.configure(bg="#F0F4F7")

        ttk.Label(assign_window, text="Select Worker:").grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
        worker_var = tk.StringVar()
        workers = [f"{w.role} #{i + 1}" for i, w in enumerate(self.selected_player.workers)]
        worker_dropdown = ttk.Combobox(assign_window, textvariable=worker_var, state="readonly")
        worker_dropdown['values'] = workers
        worker_dropdown.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)

        ttk.Label(assign_window, text="Select Factory:").grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
        factory_var = tk.StringVar()
        factories = [factory.name for factory in self.selected_player.factories]
        factory_dropdown = ttk.Combobox(assign_window, textvariable=factory_var, state="readonly")
        factory_dropdown['values'] = factories
        factory_dropdown.grid(row=1, column=1, padx=10, pady=10, sticky=tk.W)

        def assign_worker():
            if not worker_var.get() or not factory_var.get():
                messagebox.showerror("Error", "Select both worker and factory.")
                return
            try:
                worker_index = int(worker_var.get().split('#')[1]) - 1
                worker_obj = self.selected_player.workers[worker_index]
            except (IndexError, ValueError):
                messagebox.showerror("Error", "Invalid worker selection.")
                return
            factory_obj = next((f for f in self.selected_player.factories if f.name == factory_var.get()), None)
            if not factory_obj:
                messagebox.showerror("Error", "Invalid factory selected.")
                return
            role = worker_obj.role.strip()
            if role not in factory_obj.workers_required:
                messagebox.showerror("Error", f"{role} is not required for {factory_obj.name}.")
                return
            required = factory_obj.workers_required[role]
            assigned = factory_obj.workers_assigned.get(role, 0)
            if assigned >= required:
                messagebox.showerror("Error", f"No need for more {role}s in {factory_obj.name}.")
                return

            factory_obj.workers_assigned[role] = assigned + 1
            assign_window.destroy()
            self.refresh_factories()
            messagebox.showinfo("Success", f"{role} assigned to {factory_obj.name}.")

        ttk.Button(assign_window, text="Assign", command=assign_worker).grid(row=2, column=0, columnspan=2, pady=20)

    def remove_worker(self):
        if not self.selected_player:
            messagebox.showerror("Error", "No player selected.")
            return
        selected_item = self.worker_tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "No worker selected.")
            return
        worker_role = self.worker_tree.item(selected_item, 'values')[0]
        worker_obj = next((w for w in self.selected_player.workers if w.role == worker_role), None)
        if worker_obj:
            # Unassign from factories
            for factory in self.selected_player.factories:
                if worker_role in factory.workers_assigned:
                    factory.workers_assigned[worker_role] = max(factory.workers_assigned[worker_role] - 1, 0)
                    if factory.workers_assigned[worker_role] == 0:
                        del factory.workers_assigned[worker_role]
            self.selected_player.workers.remove(worker_obj)
            self.refresh_workers()
            self.refresh_factories()
            self.refresh_dashboard()
            messagebox.showinfo("Success", f"{worker_role} removed successfully.")

    # ---------------------- Technology Management ----------------------

    def purchase_technology_dialog(self):
        if not self.selected_player:
            messagebox.showerror("Error", "No player selected.")
            return

        add_window = tk.Toplevel(self)
        add_window.title("Purchase Technology")
        add_window.geometry("600x400")
        add_window.configure(bg="#F0F4F7")

        ttk.Label(add_window, text="Select Technology:").grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
        tech_type_var = tk.StringVar()
        tech_names = [tech.name for tech in self.technologies_list]
        tech_dropdown = ttk.Combobox(add_window, textvariable=tech_type_var, state="readonly")
        tech_dropdown['values'] = tech_names
        tech_dropdown.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)

        tech_details = tk.Text(add_window, width=60, height=15, wrap='word', state='disabled')
        tech_details.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        def display_tech_details(event):
            selected_tech_name = tech_type_var.get()
            tech_obj = next((t for t in self.technologies_list if t.name == selected_tech_name), None)
            if tech_obj:
                details = (
                    f"Name: {tech_obj.name}\n"
                    f"Category: {tech_obj.category}\n"
                    f"Cost: {tech_obj.cost} EC\n"
                    f"Maintenance: {tech_obj.maintenance} EC/round\n"
                    f"Effect: {tech_obj.effect}\n"
                    f"Prerequisites: {', '.join(tech_obj.prerequisites) if tech_obj.prerequisites else 'None'}"
                )
                tech_details.config(state='normal')
                tech_details.delete(1.0, tk.END)
                tech_details.insert(tk.END, details)
                tech_details.config(state='disabled')

        tech_dropdown.bind("<<ComboboxSelected>>", display_tech_details)
        display_tech_details(None)  # Display details for the default selection

        def purchase_technology():
            name = tech_type_var.get()
            if not name:
                messagebox.showerror("Error", "Please select a technology.")
                return
            tech_obj = next((t for t in self.technologies_list if t.name == name), None)
            if not tech_obj:
                messagebox.showerror("Error", "Invalid technology selected.")
                return
            if self.selected_player.ec < tech_obj.cost:
                messagebox.showerror("Error", "Not enough EC to purchase this technology.")
                return
            # Check prerequisites
            for prereq in tech_obj.prerequisites:
                has_worker = any(w.role == prereq for w in self.selected_player.workers)
                has_tech = any(t.name == prereq for t in self.selected_player.technologies)
                if not (has_worker or has_tech):
                    messagebox.showerror("Error", f"Prerequisite '{prereq}' not met.")
                    return

            # Check if technology is already purchased
            if any(t.name == tech_obj.name for t in self.selected_player.technologies):
                messagebox.showerror("Error", "Technology already purchased.")
                return

            self.selected_player.ec -= tech_obj.cost
            self.selected_player.technologies.append(tech_obj)
            add_window.destroy()
            self.refresh_technologies()
            self.refresh_dashboard()
            messagebox.showinfo("Success", f"{tech_obj.name} purchased successfully.")

        ttk.Button(add_window, text="Purchase", command=purchase_technology).grid(row=2, column=0, columnspan=2, pady=20)

    def remove_technology(self):
        if not self.selected_player:
            messagebox.showerror("Error", "No player selected.")
            return
        selected_item = self.tech_tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "No technology selected.")
            return
        tech_name = self.tech_tree.item(selected_item, 'values')[0]
        tech_obj = next((t for t in self.selected_player.technologies if t.name == tech_name), None)
        if tech_obj:
            refund = tech_obj.cost // 2  # optional partial refund
            self.selected_player.ec += refund
            self.selected_player.technologies.remove(tech_obj)
            self.refresh_technologies()
            self.refresh_dashboard()
            messagebox.showinfo("Success", f"{tech_obj.name} removed. Refunded {refund} EC.")

    # ---------------------- Resource Trading & Selling ----------------------

    def trade_resources_dialog(self):
        if not self.selected_player:
            messagebox.showerror("Error", "No player selected.")
            return

        trade_window = tk.Toplevel(self)
        trade_window.title("Trade Resources")
        trade_window.geometry("500x300")
        trade_window.configure(bg="#F0F4F7")

        ttk.Label(trade_window, text="Offer Resource:").grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
        offer_var = tk.StringVar()
        offer_dropdown = ttk.Combobox(trade_window, textvariable=offer_var, state="readonly")
        offer_dropdown['values'] = list(self.selected_player.resources.keys())
        offer_dropdown.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)

        ttk.Label(trade_window, text="Offer Quantity:").grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
        offer_qty_var = tk.StringVar()
        offer_qty_entry = ttk.Entry(trade_window, textvariable=offer_qty_var)
        offer_qty_entry.grid(row=1, column=1, padx=10, pady=10, sticky=tk.W)

        ttk.Label(trade_window, text="Request Resource:").grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)
        request_var = tk.StringVar()
        request_dropdown = ttk.Combobox(trade_window, textvariable=request_var, state="readonly")
        request_dropdown['values'] = list(self.selected_player.resources.keys())
        request_dropdown.grid(row=2, column=1, padx=10, pady=10, sticky=tk.W)

        ttk.Label(trade_window, text="Request Quantity:").grid(row=3, column=0, padx=10, pady=10, sticky=tk.W)
        request_qty_var = tk.StringVar()
        request_qty_entry = ttk.Entry(trade_window, textvariable=request_qty_var)
        request_qty_entry.grid(row=3, column=1, padx=10, pady=10, sticky=tk.W)

        def perform_trade():
            try:
                off_q = int(offer_qty_var.get())
                req_q = int(request_qty_var.get())
            except ValueError:
                messagebox.showerror("Error", "Quantities must be integers.")
                return
            if off_q <= 0 or req_q <= 0:
                messagebox.showerror("Error", "Quantities must be positive.")
                return

            off_res = offer_var.get()
            req_res = request_var.get()
            if not off_res or not req_res:
                messagebox.showerror("Error", "Select both offer and request resources.")
                return

            available_offer = self.selected_player.resources.get(off_res, 0)
            if available_offer < off_q:
                messagebox.showerror("Error", f"Not enough {off_res} to offer.")
                return

            # Basic 1:1 resource swap demonstration
            self.selected_player.resources[off_res] -= off_q
            self.selected_player.resources[req_res] += req_q

            messagebox.showinfo("Trade", f"Successfully traded {off_q} {off_res} for {req_q} {req_res}.")
            trade_window.destroy()
            self.refresh_resources()

        ttk.Button(trade_window, text="Trade", command=perform_trade).grid(row=4, column=0, columnspan=2, pady=20)

    def sell_resources_dialog(self):
        if not self.selected_player:
            messagebox.showerror("Error", "No player selected.")
            return

        sell_window = tk.Toplevel(self)
        sell_window.title("Sell Resources")
        sell_window.geometry("400x250")
        sell_window.configure(bg="#F0F4F7")

        ttk.Label(sell_window, text="Select Resource to Sell:").grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
        resource_var = tk.StringVar()
        resource_names = list(self.selected_player.resources.keys())
        resource_dropdown = ttk.Combobox(sell_window, textvariable=resource_var, state="readonly")
        resource_dropdown['values'] = resource_names
        resource_dropdown.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)

        ttk.Label(sell_window, text="Quantity to Sell:").grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
        quantity_var = tk.StringVar()
        quantity_entry = ttk.Entry(sell_window, textvariable=quantity_var)
        quantity_entry.grid(row=1, column=1, padx=10, pady=10, sticky=tk.W)

        def confirm_sale():
            res = resource_var.get()
            try:
                qty = int(quantity_var.get())
            except ValueError:
                messagebox.showerror("Error", "Quantity must be a valid integer.")
                return
            if qty <= 0:
                messagebox.showerror("Error", "Quantity must be positive.")
                return
            if self.selected_player.resources.get(res, 0) < qty:
                messagebox.showerror("Error", f"Not enough {res} to sell.")
                return

            # Sell price: 50 EC/unit
            total_sale = qty * 50
            self.selected_player.resources[res] -= qty
            self.selected_player.ec += total_sale

            messagebox.showinfo("Sale Complete", f"Sold {qty}x {res} for {total_sale} EC.")
            sell_window.destroy()
            self.refresh_resources()
            self.refresh_dashboard()

        ttk.Button(sell_window, text="Sell", command=confirm_sale).grid(row=2, column=0, columnspan=2, pady=20)

    # ---------------------- Terrain Management ----------------------

    def purchase_terrain_dialog(self):
        if not self.selected_player:
            messagebox.showerror("Error", "No player selected.")
            return

        selected_items = self.terrain_tree.selection()
        if not selected_items:
            messagebox.showerror("Error", "No terrain tile selected.")
            return

        selected = self.terrain_tree.item(selected_items[0])
        terrain_id = int(selected['values'][0]) - 1
        terrain = self.game_state.terrain_tiles[terrain_id]

        if terrain.owned_by:
            messagebox.showerror("Error", "Terrain tile already owned.")
            return

        if self.selected_player.ec < terrain.purchase_cost:
            messagebox.showerror("Error", "Not enough EC to purchase this terrain.")
            return

        def confirm_purchase():
            try:
                self.selected_player.ec -= terrain.purchase_cost
                terrain.owned_by = self.selected_player.name
                self.refresh_terrain()
                self.refresh_tabs()
                messagebox.showinfo("Success", f"Terrain tile {terrain_id + 1} purchased successfully.")
                purchase_window.destroy()
            except Exception as e:
                messagebox.showerror("Error", str(e))

        purchase_window = tk.Toplevel(self)
        purchase_window.title("Confirm Purchase")
        purchase_window.geometry("400x200")
        purchase_window.configure(bg="#F0F4F7")

        info = (
            f"Terrain ID: {terrain_id + 1}\n"
            f"Terrain Type: {terrain.terrain_type}\n"
            f"Purchase Cost: {terrain.purchase_cost} EC\n"
            f"Resources: {', '.join(terrain.resources)}\n"
            f"Carbon Offset: {terrain.carbon_offset}\n"
            f"Owned By: None"
        )
        ttk.Label(purchase_window, text="Confirm Purchase:", font=("Arial", 12, "bold")).pack(padx=10, pady=10)
        ttk.Label(purchase_window, text=info, justify=tk.LEFT).pack(padx=10, pady=5)

        ttk.Button(purchase_window, text="Confirm", command=confirm_purchase).pack(pady=10)
        ttk.Button(purchase_window, text="Cancel", command=purchase_window.destroy).pack()

    # ---------------------- Factory Management ----------------------

    def add_factory_dialog(self):
        if not self.selected_player:
            messagebox.showerror("Error", "No player selected.")
            return

        add_window = tk.Toplevel(self)
        add_window.title("Add Factory")
        add_window.geometry("700x700")
        add_window.configure(bg="#F0F4F7")

        ttk.Label(add_window, text="Select Factory Type:").grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
        factory_type_var = tk.StringVar()
        factory_types = [factory.name for factory in self.factories_list]
        factory_dropdown = ttk.Combobox(add_window, textvariable=factory_type_var, state="readonly")
        factory_dropdown['values'] = factory_types
        factory_dropdown.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)

        ttk.Label(add_window, text="Select Terrain Tile:").grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
        terrain_var = tk.StringVar()
        owned_tiles = [
            f"{i + 1}. {tile.terrain_type}"
            for i, tile in enumerate(self.game_state.terrain_tiles)
            if tile.owned_by == self.selected_player.name
        ]
        if not owned_tiles:
            owned_tiles = ["No owned terrain tiles available."]
        terrain_dropdown = ttk.Combobox(add_window, textvariable=terrain_var, state="readonly")
        terrain_dropdown['values'] = owned_tiles
        terrain_dropdown.grid(row=1, column=1, padx=10, pady=10, sticky=tk.W)

        ttk.Label(add_window, text="Select Transportation Type for Each Resource Needed:").grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)

        transportation_frames = []

        def update_transportation_fields(event):
            factory_type = factory_type_var.get()
            for trans_dropdown in transportation_frames:
                trans_dropdown.destroy()
            transportation_frames.clear()
            f_obj = next((f for f in self.factories_list if f.name == factory_type), None)
            if f_obj and f_obj.transportation_needed:
                row_start = 3
                for idx, res in enumerate(f_obj.transportation_needed):
                    lbl = ttk.Label(add_window, text=f"{res}:")
                    lbl.grid(row=row_start + idx, column=0, padx=20, pady=5, sticky=tk.W)
                    trans_var = tk.StringVar()
                    trans_dropdown = ttk.Combobox(add_window, textvariable=trans_var, state="readonly")
                    trans_dropdown['values'] = [t['type'] for t in self.transportation_types]
                    trans_dropdown.current(0)
                    trans_dropdown.grid(row=row_start + idx, column=1, padx=10, pady=5, sticky=tk.W)
                    transportation_frames.append(trans_dropdown)

        factory_dropdown.bind("<<ComboboxSelected>>", update_transportation_fields)
        update_transportation_fields(None)  # Initialize transportation fields for default selection

        def add_factory():
            fac_name = factory_type_var.get()
            terrain_selection = terrain_var.get()
            if not fac_name or not terrain_selection or terrain_selection == "No owned terrain tiles available.":
                messagebox.showerror("Error", "Please select both a factory type and a valid terrain.")
                return
            f_obj = next((f for f in self.factories_list if f.name == fac_name), None)
            if not f_obj:
                messagebox.showerror("Error", "Invalid factory type selected.")
                return

            try:
                tid = int(terrain_selection.split('.')[0]) - 1
            except (IndexError, ValueError):
                messagebox.showerror("Error", "Invalid terrain selection.")
                return
            terrain_tile = self.game_state.terrain_tiles[tid]
            if terrain_tile.terrain_type not in f_obj.allowed_terrain:
                messagebox.showerror("Error", f"{f_obj.name} cannot be placed on {terrain_tile.terrain_type} terrain.")
                return
            if self.selected_player.ec < f_obj.construction_cost:
                messagebox.showerror("Error", "Not enough EC to construct this factory.")
                return

            # Check resource requirements
            missing_resources = {}
            for r, q in f_obj.resource_requirements.items():
                if self.selected_player.resources.get(r, 0) < q:
                    missing_resources[r] = q - self.selected_player.resources.get(r, 0)

            if missing_resources:
                if not self.buy_resources_from_bank(missing_resources):
                    messagebox.showerror("Error", "Cannot proceed without required resources.")
                    return

            # Deduct resources
            for r, q in f_obj.resource_requirements.items():
                self.selected_player.resources[r] -= q

            # Deduct EC for construction
            self.selected_player.ec -= f_obj.construction_cost

            # Create a copy of the factory
            new_factory = Factory(
                name=f_obj.name,
                construction_cost=f_obj.construction_cost,
                operational_cost=f_obj.operational_cost,
                pollution=f_obj.pollution,
                output=f_obj.output.copy(),
                resource_requirements=f_obj.resource_requirements.copy(),
                allowed_terrain=f_obj.allowed_terrain.copy(),
                workers_required=f_obj.workers_required.copy(),
                transportation_needed=f_obj.transportation_needed.copy(),
                ec_output=f_obj.ec_output
            )

            # Assign transportation
            if f_obj.transportation_needed:
                for idx, r in enumerate(f_obj.transportation_needed):
                    trans_type = transportation_frames[idx].get()
                    dist, tile_idx = self.find_nearest_resource(tid, r)
                    if tile_idx is None:
                        messagebox.showerror("Error", f"No owned terrain provides {r}.")
                        # Refund
                        self.selected_player.ec += new_factory.construction_cost
                        for rr, qq in f_obj.resource_requirements.items():
                            self.selected_player.resources[rr] += qq
                        return
                    new_factory.transportation[r] = {"type": trans_type, "distance": dist}

            # ------------------ Worker Requirement Warning ------------------
            for role, count_needed in new_factory.workers_required.items():
                available_workers = [w for w in self.selected_player.workers if w.role == role]
                if len(available_workers) < count_needed:
                    messagebox.showwarning(
                        "Warning",
                        f"Not enough {role}(s) for {new_factory.name} "
                        f"(need {count_needed}, have {len(available_workers)})."
                    )

            # Attempt to auto-assign as many as possible
            for role, count_needed in new_factory.workers_required.items():
                assigned = 0
                available_workers = [w for w in self.selected_player.workers if w.role == role]
                while assigned < count_needed and available_workers:
                    worker_obj = available_workers.pop()
                    new_factory.workers_assigned[role] = new_factory.workers_assigned.get(role, 0) + 1
                    assigned += 1

            self.selected_player.factories.append(new_factory)
            add_window.destroy()
            self.refresh_factories()
            self.refresh_resources()
            self.refresh_dashboard()
            messagebox.showinfo("Success", f"{new_factory.name} added successfully.")

        ttk.Button(add_window, text="Add Factory", command=add_factory).grid(row=50, column=0, columnspan=2, pady=20)

    def find_nearest_resource(self, factory_terrain_index: int, resource: str) -> (int, Optional[int]):
        min_dist = float('inf')
        found_index = None
        for i, tile in enumerate(self.game_state.terrain_tiles):
            if tile.owned_by == self.selected_player.name and resource in tile.resources:
                d = self.calculate_distance(factory_terrain_index, i)
                if d < min_dist:
                    min_dist = d
                    found_index = i
        if found_index is None:
            return 0, None
        return min_dist, found_index

    def calculate_distance(self, index1: int, index2: int) -> int:
        row1, col1 = divmod(index1, 5)
        row2, col2 = divmod(index2, 5)
        return abs(row1 - row2) + abs(col1 - col2)

    def remove_factory(self):
        if not self.selected_player:
            messagebox.showerror("Error", "No player selected.")
            return
        selected_item = self.factory_tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "No factory selected.")
            return
        factory_name = self.factory_tree.item(selected_item, 'values')[0]
        factory_obj = next((f for f in self.selected_player.factories if f.name == factory_name), None)
        if factory_obj:
            # Optional partial refund
            self.selected_player.ec += factory_obj.construction_cost
            # Also return produced resources to the player's stock if you want,
            # but this is optional. Typically removing a factory doesn't
            # retroactively remove its outputs from the game.
            for res, qty in factory_obj.output.items():
                if res != "Consultancy Services":
                    self.selected_player.resources[res] += qty

            self.selected_player.factories.remove(factory_obj)
            self.refresh_factories()
            self.refresh_resources()
            self.refresh_dashboard()
            messagebox.showinfo("Success", f"{factory_obj.name} removed successfully.")

    def buy_resources_from_bank(self, required_resources: Dict[str, int]) -> bool:
        total_cost = 0
        resource_costs = {}
        for res, qty in required_resources.items():
            cost_per_unit = 100  # double base price
            cost = cost_per_unit * qty
            resource_costs[res] = cost
            total_cost += cost

        msg = "You need to buy these resources from the bank:\n\n"
        for res, cost in resource_costs.items():
            msg += f"{res}: {cost // 100} units => {cost} EC total\n"
        msg += f"\nTotal Cost: {total_cost} EC\nProceed?"

        if not messagebox.askyesno("Buy Resources", msg):
            return False

        if self.selected_player.ec < total_cost:
            messagebox.showerror("Error", "Not enough EC to buy required resources.")
            return False

        self.selected_player.ec -= total_cost
        for r, cost in resource_costs.items():
            qty_purchased = cost // 100
            self.selected_player.resources[r] += qty_purchased

        self.refresh_dashboard()
        self.refresh_resources()
        return True

    # ---------------------- End Game ----------------------

    def end_game(self):
        scores = []
        for player in self.game_state.players:
            score = player.ec / (1 + player.pp)
            scores.append((player.name, score))
        scores.sort(key=lambda x: x[1], reverse=True)
        winner = scores[0]
        msg = "Game Over.\n\nFinal Scores:\n"
        for name, sc in scores:
            msg += f"{name}: {sc:.2f}\n"
        msg += f"\nWinner: {winner[0]} with a score of {winner[1]:.2f}!"
        messagebox.showinfo("Game Over", msg)
        self.destroy()

# ---------------------- Main Execution ----------------------

def main():
    game_state = GameState()
    # Optionally add test players
    # game_state.add_player("Player 1")
    # game_state.add_player("Player 2")

    app = CompanionApp(game_state)
    app.mainloop()

if __name__ == "__main__":
    main()

# Sudoku Game Visual Layouts

## 1. START SCREEN (540 x 600 pixels)

```
┌─────────────────────────────────────────────┐
│                                             │
│                                             │
│         Welcome to Sudoku                   │  ← Title (y=100, centered)
│                                             │
│                                             │
│                                             │
│          ┌──────────────┐                  │
│          │    Easy      │                  │  ← Button at (170, 200)
│          └──────────────┘                  │     Size: 200 x 60
│                                             │
│          ┌──────────────┐                  │
│          │   Medium     │                  │  ← Button at (170, 300)
│          └──────────────┘                  │     Size: 200 x 60
│                                             │
│          ┌──────────────┐                  │
│          │    Hard      │                  │  ← Button at (170, 400)
│          └──────────────┘                  │     Size: 200 x 60
│                                             │
│                                             │
│                                             │
└─────────────────────────────────────────────┘
     540 pixels wide
```

**Button Details:**
- All buttons: 200 pixels wide, 60 pixels tall
- Gray background with black border (2px thick)
- Black text, Arial font, size 30
- Centered text inside button

---

## 2. GAME BOARD LAYOUT (540 x 540 pixels)

The board is a 9x9 grid divided into 3x3 boxes:

```
┌──────┬──────┬──────┐
│ 5 3  │      │ 7    │  ← Thick lines separate 3x3 boxes (8px)
│ 6    │ 1 9  │ 5    │     (lines at x=180, x=360, y=180, y=360)
│   9  │ 8    │      │
├──────┼──────┼──────┤
│ 8    │   6  │      │  ← Thin lines separate individual cells (4px)
│ 4    │ 8    │ 3    │     (lines at multiples of 60)
│ 7    │   2  │ 6    │
├──────┼──────┼──────┤
│   6  │      │ 2 8  │
│      │ 4 1  │ 9    │
│      │   5  │      │
└──────┴──────┴──────┘
  540 pixels

Cell Size: 60 x 60 pixels (540 ÷ 9 = 60)
Box Size: 180 x 180 pixels (3 cells × 60 = 180)
```

**Grid Structure:**
- **Thick black lines (8px)**: Separate the 9 major 3x3 boxes
  - Horizontal at y = 180 and y = 360
  - Vertical at x = 180 and x = 360
- **Thin black lines (4px)**: Separate individual cells
  - Horizontal at y = 60, 120, 240, 300, 420, 480
  - Vertical at x = 60, 120, 240, 300, 420, 480

**Cell Details:**
- Each cell: 60 × 60 pixels
- Numbers displayed in center if value != 0
- Sketched values (gray, small) if sketched_value != 0
- Selected cell: Red border (255, 0, 0) instead of black

---

## 3. GAME SCREEN WITH BUTTONS (540 x 600 pixels)

```
┌─────────────────────────────────────────────┐
│                                             │
│   ┌───┬───┬───┬───┬───┬───┬───┬───┬───┐   │
│   │ 5 │ 3 │   │   │ 7 │   │   │   │   │   │
│   ├───┼───┼───┼───┼───┼───┼───┼───┼───┤   │
│   │ 6 │   │   │ 1 │ 9 │ 5 │   │   │   │   │  ← Board area
│   ├───┼───┼───┼───┼───┼───┼───┼───┼───┤   │     540 x 540
│   │   │ 9 │ 8 │   │   │   │   │   │   │   │
│   ├───┼───┼───┼───┼───┼───┼───┼───┼───┤   │
│   │ 8 │   │   │   │ 6 │   │   │   │   │   │
│   ├───┼───┼───┼───┼───┼───┼───┼───┼───┤   │
│   │ 4 │   │   │ 8 │   │ 3 │   │   │   │   │
│   ├───┼───┼───┼───┼───┼───┼───┼───┼───┤   │
│   │ 7 │   │   │   │ 2 │ 6 │   │   │   │   │
│   ├───┼───┼───┼───┼───┼───┼───┼───┼───┤   │
│   │   │ 6 │   │   │   │   │ 2 │ 8 │   │   │
│   ├───┼───┼───┼───┼───┼───┼───┼───┼───┤   │
│   │   │   │   │ 4 │ 1 │ 9 │   │   │   │   │
│   ├───┼───┼───┼───┼───┼───┼───┼───┼───┤   │
│   │   │   │   │   │ 5 │   │   │   │   │   │
│   └───┴───┴───┴───┴───┴───┴───┴───┴───┘   │
│                                             │
│  ┌──────┐  ┌──────┐  ┌──────┐             │
│  │Reset │  │Restart│  │ Exit │             │  ← Buttons at y=550
│  └──────┘  └──────┘  └──────┘             │     Size: 100 x 40 each
│  (x=50)    (x=220)   (x=390)              │
└─────────────────────────────────────────────┘
     540 pixels wide x 600 pixels tall
```

**Button Layout:**
- **Reset button**: (50, 550) - 100 × 40 pixels
- **Restart button**: (220, 550) - 100 × 40 pixels  
- **Exit button**: (390, 550) - 100 × 40 pixels
- Font size: 25 (smaller than start screen buttons)

---

## 4. DETAILED CELL APPEARANCE

### Normal Cell (unselected):
```
┌─────┐
│     │  ← Black border (2px)
│  5  │  ← Number centered (large font, size 40)
│     │
└─────┘
```

### Selected Cell:
```
┌─────┐
│     │  ← RED border (2px) - indicates selection
│  5  │
│     │
└─────┘
```

### Empty Cell with Sketched Value:
```
┌─────┐
│     │  ← Black border
│     │
│  3  │  ← Small gray number (size 20) at top-left
│     │     (sketched_value, not confirmed)
└─────┘
```

### Empty Cell:
```
┌─────┐
│     │  ← Black border
│     │
│     │  ← Empty (value = 0)
│     │
└─────┘
```

---

## 5. COORDINATE SYSTEM

**Screen Coordinates:**
- (0, 0) = Top-left corner
- X increases → right
- Y increases → down

**Board Coordinates:**
- Board occupies: (0, 0) to (540, 540)
- Cell at row=0, col=0 is at screen position (0, 0)
- Cell at row=0, col=1 is at screen position (60, 0)
- Cell at row=1, col=0 is at screen position (0, 60)
- Cell at row=r, col=c is at screen position (c×60, r×60)

**Button Area:**
- Y coordinates from 540 to 600 (bottom 60 pixels)
- Click detection: if y < 540 → board, else → buttons

---

## Color Reference

- **WHITE**: (255, 255, 255) - Background
- **BLACK**: (0, 0, 0) - Text, borders
- **GRAY**: (200, 200, 200) - Button background
- **LIGHT_GRAY**: (240, 240, 240) - Alternative background (unused in current code)
- **RED**: (255, 0, 0) - Selected cell border


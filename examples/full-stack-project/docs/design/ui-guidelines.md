# PulseOps Design Guidelines

> **Notice**: Illustrative design guidelines document.

## 1. Design Philosophy

PulseOps follows an operational dashboard aesthetic focused on readability under high cognitive load:
- High contrast status indicators (Green / Amber / Red) with secondary icon cues for colorblind accessibility.
- Monospace typographic rendering for numerical metrics, IP addresses, and timestamps.
- Zero decorative animation on real-time data charts to prevent distraction during incident response.

## 2. Color Palette Tokens

- **Background Canvas**: `#0B0F19` (Dark Slate)
- **Card Surface**: `#111827` (Charcoal)
- **Border**: `#1F2937`
- **Primary Accent**: `#3B82F6` (Electric Blue)
- **Status Normal**: `#10B981` (Emerald)
- **Status Warning**: `#F59E0B` (Amber)
- **Status Critical**: `#EF4444` (Crimson)

## 3. Typography Scale

- **Headings**: `Inter`, sans-serif (font-weight: 600)
- **Body**: `Inter`, sans-serif (font-weight: 400, size: 14px)
- **Metrics & Code**: `JetBrains Mono`, monospace (size: 13px)

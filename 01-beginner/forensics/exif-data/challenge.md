# EXIF Data

**Category:** Forensics
**Difficulty:** Beginner

## Description

An image contains GPS coordinates in its metadata. Find the location where the photo was taken.

**Hint:** The GPS tags carry more than a location — the `GPSProcessingMethod` field holds a base64 string. Decode it to recover the flag.

## Objective

Find the flag.

## Challenge Files

- `challenge-files/forensics/exif-data/photo.jpg`

Download these files to begin the challenge.

## Flag Format

`CTF{...}` — submit this flag after solving the challenge.

## Requirements

See [REQUIREMENTS.md](../../../REQUIREMENTS.md) — **Ready to Solve — Files Included** section for setup details.

#!/usr/bin/env bash

uvicorn main:app --reload --host 0.0.0.0 --port $GPS_SIMULATOR_PORT
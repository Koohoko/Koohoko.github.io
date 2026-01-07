---
title: "Time Zone Converter for Meeting Scheduling"
date: 2026-01-07
permalink: /posts/2026/01/timezone-converter/
tags:
  - tools
  - productivity
---

A simple tool to convert time across different time zones and find overlapping working hours with collaborators around the world.

<style>
.tz-container {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  max-width: 100%;
  margin: 2em 0;
  padding: 1.5em;
  background: #fafaf9;
  border-radius: 8px;
  border: 1px solid #d6d3d1;
  box-sizing: border-box;
  overflow: hidden;
}

.tz-container * {
  box-sizing: border-box;
}

.tz-title-row {
  display: flex;
  align-items: baseline;
  flex-wrap: wrap;
  gap: 0.5em;
  margin-bottom: 1.5em;
}

.tz-title {
  margin: 0;
  color: #1a3a34;
  font-size: 1.2em;
  font-weight: 600;
}

.tz-subtitle {
  margin: 0;
  color: #737373;
  font-size: 0.85em;
}

.tz-detected {
  display: inline-block;
  padding: 0.2em 0.5em;
  background: #ecfdf5;
  color: #14532d;
  border-radius: 4px;
  font-size: 0.75em;
  margin-left: 0.5em;
  font-weight: normal;
}

.tz-section-header {
  display: flex;
  align-items: center;
  flex-wrap: wrap;
  gap: 0.5em;
  margin-bottom: 1em;
}

.tz-input-group {
  display: flex;
  flex-wrap: wrap;
  gap: 1em;
  margin-bottom: 1.5em;
  padding-bottom: 1.5em;
  border-bottom: 1px solid #e5e5e5;
}

.tz-input-item {
  flex: 1;
  min-width: 150px;
}

.tz-input-item label {
  display: block;
  margin-bottom: 0.4em;
  font-size: 0.85em;
  color: #525252;
  font-weight: 500;
}

.tz-input-item input,
.tz-input-item select {
  width: 100%;
  padding: 0.6em 0.8em;
  border: 1px solid #d6d3d1;
  border-radius: 4px;
  font-size: 0.95em;
  background: #fff;
  color: #292524;
  box-sizing: border-box;
}

.tz-input-item input:focus,
.tz-input-item select:focus {
  outline: none;
  border-color: #1a3a34;
  box-shadow: 0 0 0 2px rgba(26, 58, 52, 0.1);
}

.tz-section {
  margin-bottom: 1.5em;
  padding-bottom: 1.5em;
  border-bottom: 1px solid #e5e5e5;
}

.tz-section:last-child {
  border-bottom: none;
  margin-bottom: 0;
  padding-bottom: 0;
}

.tz-section-title {
  font-size: 0.95em;
  font-weight: 600;
  color: #404040;
  margin-bottom: 1em;
}

.tz-work-hours {
  display: flex;
  align-items: center;
  gap: 0.5em;
  margin-top: 1em;
  flex-wrap: wrap;
}

.tz-work-hours label {
  font-size: 0.85em;
  color: #525252;
}

.tz-work-hours input {
  width: 80px;
  max-width: 100%;
  padding: 0.4em;
  border: 1px solid #d6d3d1;
  border-radius: 4px;
  font-size: 0.9em;
}

.tz-legend {
  display: flex;
  gap: 1.5em;
  margin-bottom: 1em;
  flex-wrap: wrap;
}

.tz-legend-item {
  display: flex;
  align-items: center;
  gap: 0.4em;
  font-size: 0.8em;
  color: #525252;
}

.tz-legend-dot {
  width: 12px;
  height: 12px;
  border-radius: 3px;
}

.tz-legend-dot.working {
  background: #14532d;
}

.tz-legend-dot.outside {
  background: #a3a3a3;
}

.tz-legend-dot.overlap {
  background: #059669;
  box-shadow: 0 0 0 2px #d1fae5;
}

.tz-zones-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1em;
}

.tz-zones-title {
  font-size: 0.95em;
  color: #404040;
  font-weight: 500;
}

.tz-add-btn {
  padding: 0.4em 0.8em;
  background: #1a3a34;
  color: #fff;
  border: none;
  border-radius: 4px;
  font-size: 0.85em;
  cursor: pointer;
  transition: background 0.2s;
}

.tz-add-btn:hover {
  background: #14532d;
}

.tz-results {
  display: flex;
  flex-direction: column;
  gap: 0.8em;
}

.tz-result-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0.8em 1em;
  background: #fff;
  border: 1px solid #e5e5e5;
  border-radius: 6px;
  transition: box-shadow 0.2s;
  border-left: 4px solid #a3a3a3;
}

.tz-result-item.working-hours {
  border-left-color: #14532d;
  background: #f0fdf4;
}

.tz-result-item.overlap-hours {
  border-left-color: #059669;
  background: #ecfdf5;
  box-shadow: 0 0 0 1px #a7f3d0;
}

.tz-result-item.your-time {
  background: linear-gradient(135deg, #fafaf9 0%, #f5f5f4 100%);
  border: 1px dashed #d6d3d1;
  border-left: 4px solid #1a3a34;
}

.tz-result-item.your-time .tz-result-zone {
  font-weight: 600;
}

.tz-result-item.your-time .tz-you-badge {
  display: inline-block;
  background: #1a3a34;
  color: #fff;
  font-size: 0.7em;
  padding: 0.15em 0.5em;
  border-radius: 3px;
  margin-left: 0.5em;
  vertical-align: middle;
}

.tz-result-item:hover {
  box-shadow: 0 2px 8px rgba(0,0,0,0.06);
}

.tz-result-left {
  display: flex;
  flex-direction: column;
  gap: 0.2em;
}

.tz-result-zone {
  font-size: 0.9em;
  color: #525252;
}

.tz-result-status {
  font-size: 0.75em;
  padding: 0.2em 0.5em;
  border-radius: 3px;
  display: inline-block;
  width: fit-content;
}

.tz-result-status.working {
  background: #dcfce7;
  color: #14532d;
}

.tz-result-status.outside {
  background: #f5f5f5;
  color: #737373;
}

.tz-result-status.overlap {
  background: #a7f3d0;
  color: #065f46;
  font-weight: 500;
}

.tz-result-right {
  display: flex;
  align-items: center;
}

.tz-result-time {
  font-size: 1.1em;
  font-weight: 600;
  color: #1a3a34;
  font-family: "SF Mono", Monaco, monospace;
}

.tz-result-date {
  font-size: 0.8em;
  color: #737373;
  margin-left: 0.5em;
}

.tz-remove-btn {
  margin-left: 1em;
  padding: 0.2em 0.5em;
  background: none;
  border: 1px solid #d6d3d1;
  border-radius: 3px;
  color: #737373;
  cursor: pointer;
  font-size: 0.8em;
}

.tz-remove-btn:hover {
  background: #fee2e2;
  border-color: #fca5a5;
  color: #991b1b;
}

.tz-copy-btn {
  padding: 0.6em 1.2em;
  background: #f5f5f4;
  border: 1px solid #d6d3d1;
  border-radius: 4px;
  color: #404040;
  cursor: pointer;
  font-size: 0.9em;
  transition: all 0.2s;
}

.tz-copy-btn:hover {
  background: #e5e5e5;
}

.tz-copy-btn.copied {
  background: #14532d;
  color: #fff;
  border-color: #14532d;
}

.tz-action-buttons {
  display: flex;
  gap: 0.8em;
  margin-top: 1em;
  flex-wrap: wrap;
}

.tz-ics-btn {
  padding: 0.6em 1.2em;
  background: #1a3a34;
  border: 1px solid #1a3a34;
  border-radius: 4px;
  color: #fff;
  cursor: pointer;
  font-size: 0.9em;
  transition: all 0.2s;
}

.tz-ics-btn:hover {
  background: #14532d;
}

.tz-ics-btn.downloaded {
  background: #059669;
  border-color: #059669;
}

.tz-suggestion-result {
  padding: 1em;
  background: linear-gradient(135deg, #ecfdf5, #d1fae5);
  border: 1px solid #a7f3d0;
  border-radius: 8px;
  animation: fadeIn 0.3s ease;
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(-5px); }
  to { opacity: 1; transform: translateY(0); }
}

.tz-suggestion-title {
  font-size: 1em;
  font-weight: 600;
  color: #065f46;
  margin-bottom: 0.8em;
  display: flex;
  align-items: center;
  gap: 0.5em;
}

.tz-suggestion-time {
  font-size: 1.4em;
  font-weight: 700;
  color: #14532d;
  margin-bottom: 0.5em;
}

.tz-suggestion-detail {
  font-size: 0.85em;
  color: #525252;
  line-height: 1.6;
}

.tz-suggestion-breakdown {
  margin-top: 0.8em;
  padding-top: 0.8em;
  border-top: 1px solid #a7f3d0;
  font-size: 0.85em;
}

.tz-suggestion-options {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 1em;
  margin-top: 1em;
}

.tz-suggestion-option {
  padding: 1em;
  background: #fff;
  border: 1px solid #d6d3d1;
  border-radius: 8px;
  transition: all 0.2s;
}

.tz-suggestion-option:hover {
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
}

.tz-suggestion-option.excellent {
  border-color: #059669;
  background: linear-gradient(135deg, #ecfdf5, #d1fae5);
}

.tz-suggestion-option.good {
  border-color: #14532d;
  background: #f0fdf4;
}

.tz-suggestion-option.acceptable {
  border-color: #ca8a04;
  background: #fefce8;
}

.tz-suggestion-option.challenging {
  border-color: #ea580c;
  background: #fff7ed;
}

.tz-suggestion-option.difficult {
  border-color: #dc2626;
  background: #fef2f2;
}

.tz-suggestion-option.disabled {
  background: #f5f5f4;
  border-color: #d6d3d1;
}

.tz-suggestion-option-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 0.5em;
}

.tz-suggestion-option-title {
  font-weight: 600;
  font-size: 0.95em;
  color: #404040;
}

.tz-suggestion-option .tz-suggestion-time {
  font-size: 1.2em;
  margin-bottom: 0.5em;
}

.tz-suggestion-option .tz-suggestion-breakdown {
  border-top-color: #e5e5e5;
  margin-top: 0.5em;
  padding-top: 0.5em;
}

.tz-apply-btn {
  margin-top: 0.8em;
  padding: 0.5em 1em;
  background: #1a3a34;
  color: #fff;
  border: none;
  border-radius: 4px;
  font-size: 0.85em;
  cursor: pointer;
  transition: background 0.2s;
  width: 100%;
}

.tz-apply-btn:hover {
  background: #14532d;
}

.tz-apply-btn.applied {
  background: #059669;
  cursor: default;
}

.tz-apply-btn.applied:hover {
  background: #059669;
}

.tz-more-options {
  margin-top: 1em;
  padding-top: 1em;
  border-top: 1px dashed #d6d3d1;
}

.tz-more-options-title {
  font-size: 0.85em;
  color: #737373;
  margin-bottom: 0.6em;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 0.3em;
}

.tz-more-options-title:hover {
  color: #525252;
}

.tz-more-options-list {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5em;
}

.tz-mini-option {
  display: inline-flex;
  align-items: center;
  gap: 0.4em;
  padding: 0.4em 0.7em;
  background: #fff;
  border: 1px solid #e5e5e5;
  border-radius: 4px;
  font-size: 0.8em;
  cursor: pointer;
  transition: all 0.2s;
}

.tz-mini-option:hover {
  border-color: #1a3a34;
  background: #f0fdf4;
}

.tz-mini-option.applied {
  background: #059669;
  border-color: #059669;
  color: #fff;
}

.tz-mini-option-time {
  font-weight: 600;
  font-family: "SF Mono", Monaco, monospace;
}

.tz-mini-option-quality {
  font-size: 0.9em;
}

.tz-suggestion-score {
  display: inline-block;
  padding: 0.2em 0.6em;
  background: #14532d;
  color: #fff;
  border-radius: 4px;
  font-size: 0.8em;
}

.tz-priority-selector {
  display: flex;
  align-items: center;
  gap: 0.8em;
  margin-bottom: 1em;
  padding: 0.8em;
  background: #f5f5f4;
  border-radius: 6px;
  flex-wrap: wrap;
}

.tz-priority-selector label {
  font-size: 0.9em;
  color: #404040;
}

.tz-priority-selector select {
  padding: 0.5em 0.8em;
  border: 1px solid #d6d3d1;
  border-radius: 4px;
  font-size: 0.9em;
  background: #fff;
  min-width: 180px;
}

.tz-focus-checkbox {
  display: flex;
  align-items: center;
  gap: 0.4em;
  margin-left: auto;
  padding: 0.4em 0.8em;
  background: #fff;
  border: 1px solid #d6d3d1;
  border-radius: 4px;
  cursor: pointer;
  transition: all 0.2s;
}

.tz-focus-checkbox:hover {
  border-color: #14532d;
}

.tz-focus-checkbox.checked {
  background: #ecfdf5;
  border-color: #14532d;
}

.tz-focus-checkbox input {
  margin: 0;
  cursor: pointer;
}

.tz-focus-checkbox span {
  font-size: 0.85em;
  color: #404040;
  white-space: nowrap;
}

/* Mobile responsive styles */
@media (max-width: 600px) {
  .tz-container {
    padding: 1em;
    overflow-x: hidden;
  }
  
  .tz-title {
    font-size: 1.2em;
  }
  
  .tz-section {
    padding: 0.8em;
    overflow: hidden;
  }
  
  .tz-input-group {
    flex-direction: column;
    gap: 0.8em;
    margin-bottom: 1em;
    padding-bottom: 1em;
  }
  
  .tz-input-item {
    width: 100%;
    min-width: 0;
  }
  
  .tz-input-item select,
  .tz-input-item input {
    width: 100%;
    max-width: 100%;
    box-sizing: border-box;
    -webkit-appearance: none;
    -moz-appearance: none;
    appearance: none;
  }
  
  /* Fix for date/time inputs on mobile */
  .tz-input-item input[type="date"],
  .tz-input-item input[type="time"] {
    min-width: 0;
    width: 100%;
    max-width: 100%;
  }
  
  .tz-work-hours {
    flex-direction: column;
    align-items: stretch;
    gap: 0.5em;
  }
  
  .tz-work-hours label {
    margin-bottom: 0.3em;
  }
  
  .tz-work-hours input {
    width: 100%;
    max-width: 100%;
    box-sizing: border-box;
    -webkit-appearance: none;
    -moz-appearance: none;
    appearance: none;
  }
  
  .tz-work-hours input[type="time"] {
    min-width: 0;
    width: 100%;
  }
  
  .tz-result-item {
    flex-direction: column;
    align-items: flex-start;
    gap: 0.5em;
    padding: 0.8em;
  }
  
  .tz-result-right {
    width: 100%;
    justify-content: space-between;
  }
  
  .tz-result-time {
    font-size: 1.2em;
  }
  
  .tz-remove-btn {
    margin-left: auto;
  }
  
  .tz-legend {
    flex-direction: column;
    gap: 0.5em;
  }
  
  .tz-priority-selector {
    flex-direction: column;
    align-items: stretch;
    gap: 0.6em;
  }
  
  .tz-priority-selector select {
    width: 100%;
    min-width: unset;
    box-sizing: border-box;
  }
  
  .tz-focus-checkbox {
    margin-left: 0;
    justify-content: center;
  }
  
  .tz-suggestion-result {
    padding: 0.8em;
    overflow: hidden;
  }
  
  .tz-suggestion-options {
    grid-template-columns: 1fr;
    gap: 0.8em;
    margin-top: 0.8em;
  }
  
  .tz-suggestion-option {
    padding: 0.8em;
    width: 100%;
    box-sizing: border-box;
  }
  
  .tz-suggestion-option-header {
    flex-direction: column;
    align-items: flex-start;
    gap: 0.3em;
  }
  
  .tz-suggestion-score {
    align-self: flex-start;
  }
  
  .tz-suggestion-time {
    font-size: 1.1em !important;
  }
  
  .tz-suggestion-breakdown {
    font-size: 0.8em;
  }
  
  .tz-copy-btn {
    width: 100%;
    text-align: center;
    box-sizing: border-box;
  }
  
  .tz-action-buttons {
    flex-direction: column;
  }
  
  .tz-ics-btn {
    width: 100%;
    text-align: center;
    box-sizing: border-box;
  }
  
  .tz-zones-header {
    flex-direction: column;
    gap: 0.5em;
    align-items: stretch;
  }
  
  .tz-add-btn {
    width: 100%;
    text-align: center;
  }
}

/* Extra small screens */
@media (max-width: 380px) {
  .tz-container {
    padding: 0.8em;
  }
  
  .tz-section {
    padding: 0.6em;
  }
  
  .tz-result-time {
    font-size: 1em;
  }
  
  .tz-result-date {
    font-size: 0.7em;
  }
}
</style>

<div class="tz-container">
  <div class="tz-title-row">
    <h3 class="tz-title">🌍 Time Zone Converter</h3>
    <span class="tz-subtitle">— Find the best meeting time across time zones</span>
  </div>
  
  <!-- Section 1: Your Settings -->
  <div class="tz-section">
    <div class="tz-section-header">
      <div class="tz-section-title" style="margin-bottom:0;">📍 Your Settings</div>
      <span class="tz-detected" id="tz-detected"></span>
    </div>
    <div class="tz-input-group">
      <div class="tz-input-item">
        <label for="tz-source">Your City</label>
        <select id="tz-source"></select>
      </div>
      <div class="tz-input-item">
        <label for="tz-date">Date</label>
        <input type="date" id="tz-date">
      </div>
      <div class="tz-input-item">
        <label for="tz-time">Time</label>
        <input type="time" id="tz-time" value="10:00">
      </div>
    </div>
    <div class="tz-work-hours">
      <label>Working hours for everyone:</label>
      <input type="time" id="tz-work-start" value="09:00">
      <span>to</span>
      <input type="time" id="tz-work-end" value="17:00">
    </div>
  </div>
  
  <!-- Section 2: Collaborators -->
  <div class="tz-section">
    <div class="tz-zones-header">
      <div class="tz-section-title">👥 Collaborators</div>
      <button class="tz-add-btn" onclick="addTargetZone()">+ Add City</button>
    </div>
    
    <div class="tz-results" id="tz-results"></div>
    
    <div class="tz-legend" id="tz-legend" style="display:none;">
      <div class="tz-legend-item">
        <div class="tz-legend-dot working"></div>
        <span>In working hours</span>
      </div>
      <div class="tz-legend-item">
        <div class="tz-legend-dot outside"></div>
        <span>Outside working hours</span>
      </div>
    </div>
    
    <div class="tz-action-buttons" id="tz-action-buttons" style="display:none;">
      <button class="tz-copy-btn" id="tz-copy-btn" onclick="copyResults()">📋 Copy All Times</button>
      <button class="tz-ics-btn" id="tz-ics-btn" onclick="downloadICS()">📅 Download .ics</button>
    </div>
  </div>
  
  <!-- Section 3: Best Time Suggestions (auto-shown when collaborators added) -->
  <div class="tz-section" id="tz-suggestion-section" style="display:none;">
    <div class="tz-section-title">🎯 Best Meeting Times</div>
    
    <div class="tz-priority-selector">
      <label for="tz-priority">Priority participant:</label>
      <select id="tz-priority">
        <option value="none">⚖️ Everyone equally</option>
      </select>
      <label class="tz-focus-checkbox" id="tz-force-work-label" style="display:none;">
        <input type="checkbox" id="tz-force-work">
        <span>Must be in their working hours</span>
      </label>
    </div>
    
    <div id="tz-suggestion-result"></div>
  </div>
</div>

<script>
// Comprehensive list of world cities with timezones
const worldCities = [
  // Asia
  { value: 'Asia/Hong_Kong', label: 'Hong Kong', country: 'China' },
  { value: 'Asia/Shanghai', label: 'Shanghai', country: 'China' },
  { value: 'Asia/Shanghai', label: 'Beijing', country: 'China' },
  { value: 'Asia/Shanghai', label: 'Shenzhen', country: 'China' },
  { value: 'Asia/Shanghai', label: 'Guangzhou', country: 'China' },
  { value: 'Asia/Shanghai', label: 'Chongqing', country: 'China' },
  { value: 'Asia/Taipei', label: 'Taipei', country: 'Taiwan' },
  { value: 'Asia/Tokyo', label: 'Tokyo', country: 'Japan' },
  { value: 'Asia/Tokyo', label: 'Osaka', country: 'Japan' },
  { value: 'Asia/Seoul', label: 'Seoul', country: 'South Korea' },
  { value: 'Asia/Seoul', label: 'Busan', country: 'South Korea' },
  { value: 'Asia/Singapore', label: 'Singapore', country: 'Singapore' },
  { value: 'Asia/Kuala_Lumpur', label: 'Kuala Lumpur', country: 'Malaysia' },
  { value: 'Asia/Bangkok', label: 'Bangkok', country: 'Thailand' },
  { value: 'Asia/Ho_Chi_Minh', label: 'Ho Chi Minh City', country: 'Vietnam' },
  { value: 'Asia/Bangkok', label: 'Hanoi', country: 'Vietnam' },
  { value: 'Asia/Jakarta', label: 'Jakarta', country: 'Indonesia' },
  { value: 'Asia/Manila', label: 'Manila', country: 'Philippines' },
  { value: 'Asia/Kolkata', label: 'Mumbai', country: 'India' },
  { value: 'Asia/Kolkata', label: 'Delhi', country: 'India' },
  { value: 'Asia/Kolkata', label: 'Bangalore', country: 'India' },
  { value: 'Asia/Kolkata', label: 'Hyderabad', country: 'India' },
  { value: 'Asia/Kolkata', label: 'Chennai', country: 'India' },
  { value: 'Asia/Kolkata', label: 'Kolkata', country: 'India' },
  { value: 'Asia/Kolkata', label: 'Pune', country: 'India' },
  { value: 'Asia/Dhaka', label: 'Dhaka', country: 'Bangladesh' },
  { value: 'Asia/Karachi', label: 'Karachi', country: 'Pakistan' },
  { value: 'Asia/Karachi', label: 'Lahore', country: 'Pakistan' },
  { value: 'Asia/Dubai', label: 'Dubai', country: 'UAE' },
  { value: 'Asia/Dubai', label: 'Abu Dhabi', country: 'UAE' },
  { value: 'Asia/Riyadh', label: 'Riyadh', country: 'Saudi Arabia' },
  { value: 'Asia/Jerusalem', label: 'Tel Aviv', country: 'Israel' },
  { value: 'Asia/Jerusalem', label: 'Jerusalem', country: 'Israel' },
  { value: 'Asia/Tehran', label: 'Tehran', country: 'Iran' },
  { value: 'Europe/Istanbul', label: 'Istanbul', country: 'Turkey' },
  
  // Europe
  { value: 'Europe/London', label: 'London', country: 'UK' },
  { value: 'Europe/London', label: 'Cambridge', country: 'UK' },
  { value: 'Europe/London', label: 'Oxford', country: 'UK' },
  { value: 'Europe/London', label: 'Birmingham', country: 'UK' },
  { value: 'Europe/London', label: 'Bristol', country: 'UK' },
  { value: 'Europe/London', label: 'Leeds', country: 'UK' },
  { value: 'Europe/London', label: 'Liverpool', country: 'UK' },
  { value: 'Europe/London', label: 'Manchester', country: 'UK' },
  { value: 'Europe/London', label: 'Glasgow', country: 'UK' },
  { value: 'Europe/London', label: 'Edinburgh', country: 'UK' },
  { value: 'Europe/Dublin', label: 'Dublin', country: 'Ireland' },
  { value: 'Europe/Paris', label: 'Paris', country: 'France' },
  { value: 'Europe/Paris', label: 'Lyon', country: 'France' },
  { value: 'Europe/Berlin', label: 'Berlin', country: 'Germany' },
  { value: 'Europe/Berlin', label: 'Munich', country: 'Germany' },
  { value: 'Europe/Berlin', label: 'Frankfurt', country: 'Germany' },
  { value: 'Europe/Berlin', label: 'Hamburg', country: 'Germany' },
  { value: 'Europe/Zurich', label: 'Zurich', country: 'Switzerland' },
  { value: 'Europe/Zurich', label: 'Geneva', country: 'Switzerland' },
  { value: 'Europe/Amsterdam', label: 'Amsterdam', country: 'Netherlands' },
  { value: 'Europe/Amsterdam', label: 'Rotterdam', country: 'Netherlands' },
  { value: 'Europe/Amsterdam', label: 'Utrecht', country: 'Netherlands' },
  { value: 'Europe/Amsterdam', label: 'Leiden', country: 'Netherlands' },
  { value: 'Europe/Brussels', label: 'Brussels', country: 'Belgium' },
  { value: 'Europe/Brussels', label: 'Leuven', country: 'Belgium' },
  { value: 'Europe/Vienna', label: 'Vienna', country: 'Austria' },
  { value: 'Europe/Rome', label: 'Rome', country: 'Italy' },
  { value: 'Europe/Rome', label: 'Milan', country: 'Italy' },
  { value: 'Europe/Madrid', label: 'Madrid', country: 'Spain' },
  { value: 'Europe/Madrid', label: 'Barcelona', country: 'Spain' },
  { value: 'Europe/Lisbon', label: 'Lisbon', country: 'Portugal' },
  { value: 'Europe/Stockholm', label: 'Stockholm', country: 'Sweden' },
  { value: 'Europe/Oslo', label: 'Oslo', country: 'Norway' },
  { value: 'Europe/Copenhagen', label: 'Copenhagen', country: 'Denmark' },
  { value: 'Europe/Helsinki', label: 'Helsinki', country: 'Finland' },
  { value: 'Europe/Warsaw', label: 'Warsaw', country: 'Poland' },
  { value: 'Europe/Prague', label: 'Prague', country: 'Czech Republic' },
  { value: 'Europe/Budapest', label: 'Budapest', country: 'Hungary' },
  { value: 'Europe/Athens', label: 'Athens', country: 'Greece' },
  { value: 'Europe/Moscow', label: 'Moscow', country: 'Russia' },
  { value: 'Europe/Moscow', label: 'St Petersburg', country: 'Russia' },
  
  // North America
  { value: 'America/New_York', label: 'New York', country: 'USA' },
  { value: 'America/New_York', label: 'Boston', country: 'USA' },
  { value: 'America/New_York', label: 'Cambridge MA', country: 'USA' },
  { value: 'America/New_York', label: 'New Haven', country: 'USA' },
  { value: 'America/New_York', label: 'Princeton', country: 'USA' },
  { value: 'America/New_York', label: 'Philadelphia', country: 'USA' },
  { value: 'America/New_York', label: 'Baltimore', country: 'USA' },
  { value: 'America/New_York', label: 'Washington DC', country: 'USA' },
  { value: 'America/New_York', label: 'Pittsburgh', country: 'USA' },
  { value: 'America/New_York', label: 'Durham NC', country: 'USA' },
  { value: 'America/New_York', label: 'Chapel Hill', country: 'USA' },
  { value: 'America/New_York', label: 'Miami', country: 'USA' },
  { value: 'America/New_York', label: 'Atlanta', country: 'USA' },
  { value: 'America/Chicago', label: 'Chicago', country: 'USA' },
  { value: 'America/Chicago', label: 'Ann Arbor', country: 'USA' },
  { value: 'America/Chicago', label: 'Madison', country: 'USA' },
  { value: 'America/Chicago', label: 'Minneapolis', country: 'USA' },
  { value: 'America/Chicago', label: 'Houston', country: 'USA' },
  { value: 'America/Chicago', label: 'Dallas', country: 'USA' },
  { value: 'America/Chicago', label: 'Austin', country: 'USA' },
  { value: 'America/Denver', label: 'Denver', country: 'USA' },
  { value: 'America/Denver', label: 'Boulder', country: 'USA' },
  { value: 'America/Denver', label: 'Salt Lake City', country: 'USA' },
  { value: 'America/Phoenix', label: 'Phoenix', country: 'USA' },
  { value: 'America/Los_Angeles', label: 'Los Angeles', country: 'USA' },
  { value: 'America/Los_Angeles', label: 'San Francisco', country: 'USA' },
  { value: 'America/Los_Angeles', label: 'Berkeley', country: 'USA' },
  { value: 'America/Los_Angeles', label: 'Stanford', country: 'USA' },
  { value: 'America/Los_Angeles', label: 'San Diego', country: 'USA' },
  { value: 'America/Los_Angeles', label: 'Seattle', country: 'USA' },
  { value: 'America/Los_Angeles', label: 'Portland', country: 'USA' },
  { value: 'America/Anchorage', label: 'Anchorage', country: 'USA' },
  { value: 'Pacific/Honolulu', label: 'Honolulu', country: 'USA' },
  { value: 'America/Toronto', label: 'Toronto', country: 'Canada' },
  { value: 'America/Toronto', label: 'Montreal', country: 'Canada' },
  { value: 'America/Toronto', label: 'Ottawa', country: 'Canada' },
  { value: 'America/Vancouver', label: 'Vancouver', country: 'Canada' },
  { value: 'America/Edmonton', label: 'Calgary', country: 'Canada' },
  { value: 'America/Edmonton', label: 'Edmonton', country: 'Canada' },
  { value: 'America/Mexico_City', label: 'Mexico City', country: 'Mexico' },
  
  // South America
  { value: 'America/Sao_Paulo', label: 'São Paulo', country: 'Brazil' },
  { value: 'America/Sao_Paulo', label: 'Rio de Janeiro', country: 'Brazil' },
  { value: 'America/Argentina/Buenos_Aires', label: 'Buenos Aires', country: 'Argentina' },
  { value: 'America/Santiago', label: 'Santiago', country: 'Chile' },
  { value: 'America/Lima', label: 'Lima', country: 'Peru' },
  { value: 'America/Bogota', label: 'Bogota', country: 'Colombia' },
  
  // Oceania
  { value: 'Australia/Sydney', label: 'Sydney', country: 'Australia' },
  { value: 'Australia/Melbourne', label: 'Melbourne', country: 'Australia' },
  { value: 'Australia/Brisbane', label: 'Brisbane', country: 'Australia' },
  { value: 'Australia/Perth', label: 'Perth', country: 'Australia' },
  { value: 'Australia/Adelaide', label: 'Adelaide', country: 'Australia' },
  { value: 'Australia/Sydney', label: 'Canberra', country: 'Australia' },
  { value: 'Australia/Hobart', label: 'Hobart', country: 'Australia' },
  { value: 'Pacific/Auckland', label: 'Auckland', country: 'New Zealand' },
  { value: 'Pacific/Auckland', label: 'Wellington', country: 'New Zealand' },
  { value: 'Pacific/Auckland', label: 'Christchurch', country: 'New Zealand' },
  
  // Africa
  { value: 'Africa/Cairo', label: 'Cairo', country: 'Egypt' },
  { value: 'Africa/Johannesburg', label: 'Johannesburg', country: 'South Africa' },
  { value: 'Africa/Cape_Town', label: 'Cape Town', country: 'South Africa' },
  { value: 'Africa/Lagos', label: 'Lagos', country: 'Nigeria' },
  { value: 'Africa/Nairobi', label: 'Nairobi', country: 'Kenya' },
  { value: 'Africa/Casablanca', label: 'Casablanca', country: 'Morocco' },
];

let targetZones = [];  // Start with empty list
let userTimezone = '';

function init() {
  // Detect user timezone
  userTimezone = Intl.DateTimeFormat().resolvedOptions().timeZone;
  const userCity = worldCities.find(c => c.value === userTimezone);
  const detectedDiv = document.getElementById('tz-detected');
  detectedDiv.textContent = `Detected: ${userCity ? `${userCity.label}, ${userCity.country}` : userTimezone}`;
  
  // Populate source select with search
  populateSourceSelect();
  
  // Set default date to today
  const today = new Date().toISOString().split('T')[0];
  document.getElementById('tz-date').value = today;
  
  // Add event listeners for all inputs - auto update everything
  const autoUpdateHandler = () => {
    updateResults();
    autoUpdateBestTime();
  };
  
  document.getElementById('tz-date').addEventListener('change', autoUpdateHandler);
  document.getElementById('tz-time').addEventListener('change', autoUpdateHandler);
  document.getElementById('tz-source').addEventListener('change', autoUpdateHandler);
  document.getElementById('tz-work-start').addEventListener('change', autoUpdateHandler);
  document.getElementById('tz-work-end').addEventListener('change', autoUpdateHandler);
  
  // Setup force work hours checkbox styling and auto-update
  const forceWorkCheckbox = document.getElementById('tz-force-work');
  const forceWorkLabel = document.getElementById('tz-force-work-label');
  forceWorkCheckbox.addEventListener('change', () => {
    forceWorkLabel.classList.toggle('checked', forceWorkCheckbox.checked);
    autoUpdateBestTime();
  });
  // Initialize checked state
  forceWorkLabel.classList.toggle('checked', forceWorkCheckbox.checked);
  
  // Add event listener for priority selector change
  document.getElementById('tz-priority').addEventListener('change', () => {
    updateForceWorkVisibility();
    autoUpdateBestTime();
  });
  
  updateResults();
}

// Auto-update best time when inputs change
function autoUpdateBestTime() {
  if (targetZones.length > 0) {
    suggestBestTime();
  }
}

function populateSourceSelect() {
  const sourceSelect = document.getElementById('tz-source');
  const uniqueTimezones = [...new Map(worldCities.map(c => [c.value, c])).values()];
  
  uniqueTimezones.forEach(tz => {
    const option = document.createElement('option');
    option.value = tz.value;
    option.textContent = `${tz.label}, ${tz.country}`;
    sourceSelect.appendChild(option);
  });
  
  // Set default to user's timezone
  const hasUserTz = uniqueTimezones.some(tz => tz.value === userTimezone);
  sourceSelect.value = hasUserTz ? userTimezone : 'Asia/Hong_Kong';
}

function getTimeInZone(date, timezone) {
  try {
    const formatter = new Intl.DateTimeFormat('en-US', {
      timeZone: timezone,
      hour: '2-digit',
      minute: '2-digit',
      hour12: false
    });
    const parts = formatter.formatToParts(date);
    const hour = parseInt(parts.find(p => p.type === 'hour').value);
    const minute = parseInt(parts.find(p => p.type === 'minute').value);
    return hour * 60 + minute;
  } catch (e) {
    return 0;
  }
}

function isWorkingHours(timeInMinutes, workStart, workEnd) {
  return timeInMinutes >= workStart && timeInMinutes <= workEnd;
}

function updateResults() {
  const dateStr = document.getElementById('tz-date').value;
  const timeStr = document.getElementById('tz-time').value;
  const sourceTz = document.getElementById('tz-source').value;
  const workStartStr = document.getElementById('tz-work-start').value;
  const workEndStr = document.getElementById('tz-work-end').value;
  
  if (!dateStr || !timeStr) return;
  
  const workStart = parseInt(workStartStr.split(':')[0]) * 60 + parseInt(workStartStr.split(':')[1]);
  const workEnd = parseInt(workEndStr.split(':')[0]) * 60 + parseInt(workEndStr.split(':')[1]);
  
  const resultsDiv = document.getElementById('tz-results');
  resultsDiv.innerHTML = '';
  
  // If no collaborators, show empty state and hide sections
  if (targetZones.length === 0) {
    resultsDiv.innerHTML = '<div style="color:#737373;font-size:0.9em;padding:1em;text-align:center;background:#f5f5f4;border-radius:6px;">Click "+ Add City" to add collaborator locations.</div>';
    document.getElementById('tz-suggestion-section').style.display = 'none';
    document.getElementById('tz-legend').style.display = 'none';
    document.getElementById('tz-action-buttons').style.display = 'none';
    document.getElementById('tz-suggestion-result').innerHTML = '';
    return;
  }
  
  // Show sections and update priority selector
  document.getElementById('tz-suggestion-section').style.display = 'block';
  document.getElementById('tz-legend').style.display = 'flex';
  document.getElementById('tz-action-buttons').style.display = 'flex';
  updatePrioritySelector();
  
  // Create date in source timezone
  const sourceDate = new Date(`${dateStr}T${timeStr}:00`);
  
  // Check source timezone working hours
  const sourceTimeMinutes = getTimeInZone(sourceDate, sourceTz);
  const sourceIsWorking = isWorkingHours(sourceTimeMinutes, workStart, workEnd);
  
  // Check all target zones
  let allInWorkingHours = sourceIsWorking;
  const zoneResults = [];
  
  targetZones.forEach((tz, index) => {
    const cityInfo = worldCities.find(c => c.value === tz.value && c.label === tz.label);
    const tzLabel = cityInfo ? `${cityInfo.label}, ${cityInfo.country}` : tz.label;
    const timeInMinutes = getTimeInZone(sourceDate, tz.value);
    const isWorking = isWorkingHours(timeInMinutes, workStart, workEnd);
    
    if (!isWorking) allInWorkingHours = false;
    
    const targetFormatter = new Intl.DateTimeFormat('en-US', {
      timeZone: tz.value,
      weekday: 'short',
      month: 'short',
      day: 'numeric',
      hour: '2-digit',
      minute: '2-digit',
      hour12: false
    });
    
    const formatted = targetFormatter.format(sourceDate);
    const parts = formatted.split(', ');
    const dayDate = parts.slice(0, 2).join(', ');
    const time = parts[2] || parts[1];
    
    zoneResults.push({
      tz: tz.value, tzLabel, time, dayDate, isWorking, index
    });
  });
  
  // Render user's own time first
  const sourceFormatter = new Intl.DateTimeFormat('en-US', {
    timeZone: sourceTz,
    weekday: 'short',
    month: 'short',
    day: 'numeric',
    hour: '2-digit',
    minute: '2-digit',
    hour12: false
  });
  const sourceFormatted = sourceFormatter.format(sourceDate);
  const sourceParts = sourceFormatted.split(', ');
  const sourceDayDate = sourceParts.slice(0, 2).join(', ');
  const sourceTime = sourceParts[2] || sourceParts[1];
  const sourceCityInfo = worldCities.find(c => c.value === sourceTz);
  const sourceLabel = sourceCityInfo ? `${sourceCityInfo.label}, ${sourceCityInfo.country}` : sourceTz.split('/').pop().replace(/_/g, ' ');
  
  const yourStatusClass = sourceIsWorking ? 'working' : 'outside';
  const yourStatusText = sourceIsWorking ? '✓ Working hours' : '○ Outside hours';
  
  const yourItem = document.createElement('div');
  yourItem.className = `tz-result-item your-time ${sourceIsWorking ? 'working-hours' : ''}`;
  yourItem.innerHTML = `
    <div class="tz-result-left">
      <span class="tz-result-zone">${sourceLabel}<span class="tz-you-badge">You</span></span>
      <span class="tz-result-status ${yourStatusClass}">${yourStatusText}</span>
    </div>
    <div class="tz-result-right">
      <span class="tz-result-time">${sourceTime}</span>
      <span class="tz-result-date">${sourceDayDate}</span>
    </div>
  `;
  resultsDiv.appendChild(yourItem);
  
  // Render collaborators results
  zoneResults.forEach(result => {
    const statusClass = result.isWorking ? 'working' : 'outside';
    const statusText = result.isWorking ? '✓ Working hours' : '○ Outside hours';
    const itemClass = result.isWorking ? 'working-hours' : '';
    
    const item = document.createElement('div');
    item.className = `tz-result-item ${itemClass}`;
    item.innerHTML = `
      <div class="tz-result-left">
        <span class="tz-result-zone">${result.tzLabel}</span>
        <span class="tz-result-status ${statusClass}">${statusText}</span>
      </div>
      <div class="tz-result-right">
        <span class="tz-result-time">${result.time}</span>
        <span class="tz-result-date">${result.dayDate}</span>
        <button class="tz-remove-btn" onclick="removeZone(${result.index})">✕</button>
      </div>
    `;
    resultsDiv.appendChild(item);
  });
}

function formatMinutes(minutes) {
  const h = Math.floor(minutes / 60);
  const m = minutes % 60;
  return `${h.toString().padStart(2, '0')}:${m.toString().padStart(2, '0')}`;
}

function addTargetZone() {
  // Create search container
  const container = document.createElement('div');
  container.className = 'tz-search-container';
  container.style.cssText = 'margin-bottom:1em;padding:1em;background:#fff;border:1px solid #d6d3d1;border-radius:6px;';
  
  const searchInput = document.createElement('input');
  searchInput.type = 'text';
  searchInput.placeholder = 'Search city name... (↑↓ to navigate, Enter to select)';
  searchInput.style.cssText = 'width:100%;padding:0.6em;border:1px solid #d6d3d1;border-radius:4px;font-size:0.95em;box-sizing:border-box;';
  
  const resultsList = document.createElement('div');
  resultsList.style.cssText = 'max-height:200px;overflow-y:auto;margin-top:0.5em;border:1px solid #e5e5e5;border-radius:4px;display:none;';
  
  const btnContainer = document.createElement('div');
  btnContainer.style.cssText = 'display:flex;justify-content:flex-end;margin-top:0.5em;';
  
  const cancelBtn = document.createElement('button');
  cancelBtn.textContent = 'Cancel';
  cancelBtn.style.cssText = 'padding:0.4em 0.8em;background:#f5f5f4;border:1px solid #d6d3d1;border-radius:4px;cursor:pointer;font-size:0.85em;';
  cancelBtn.onclick = () => container.remove();
  btnContainer.appendChild(cancelBtn);
  
  let currentMatches = [];
  let selectedIndex = -1;
  
  const updateSelection = () => {
    const items = resultsList.querySelectorAll('.tz-search-item');
    items.forEach((item, index) => {
      if (index === selectedIndex) {
        item.style.background = '#ecfdf5';
        item.style.borderLeft = '3px solid #14532d';
        // Scroll into view if needed
        item.scrollIntoView({ block: 'nearest' });
      } else {
        item.style.background = '#fff';
        item.style.borderLeft = 'none';
      }
    });
  };
  
  const selectCity = (city) => {
    targetZones.push({ value: city.value, label: city.label });
    container.remove();
    updateResults();
    autoUpdateBestTime();
  };
  
  searchInput.addEventListener('keydown', (e) => {
    if (currentMatches.length === 0) return;
    
    if (e.key === 'ArrowDown') {
      e.preventDefault();
      selectedIndex = Math.min(selectedIndex + 1, currentMatches.length - 1);
      updateSelection();
    } else if (e.key === 'ArrowUp') {
      e.preventDefault();
      selectedIndex = Math.max(selectedIndex - 1, 0);
      updateSelection();
    } else if (e.key === 'Enter') {
      e.preventDefault();
      if (selectedIndex >= 0 && selectedIndex < currentMatches.length) {
        selectCity(currentMatches[selectedIndex]);
      } else if (currentMatches.length > 0) {
        // If nothing selected, select first match
        selectCity(currentMatches[0]);
      }
    } else if (e.key === 'Escape') {
      container.remove();
    }
  });
  
  searchInput.addEventListener('input', () => {
    const query = searchInput.value.toLowerCase().trim();
    resultsList.innerHTML = '';
    selectedIndex = -1;
    currentMatches = [];
    
    if (query.length < 1) {
      resultsList.style.display = 'none';
      return;
    }
    
    currentMatches = worldCities.filter(c => {
      const searchStr = `${c.label} ${c.country}`.toLowerCase();
      const alreadyAdded = targetZones.some(t => t.value === c.value && t.label === c.label);
      return searchStr.includes(query) && !alreadyAdded;
    }).slice(0, 10);
    
    if (currentMatches.length === 0) {
      resultsList.innerHTML = '<div style="padding:0.8em;color:#737373;font-size:0.9em;">No matching cities found</div>';
      resultsList.style.display = 'block';
      return;
    }
    
    currentMatches.forEach((city, index) => {
      const item = document.createElement('div');
      item.className = 'tz-search-item';
      item.style.cssText = 'padding:0.6em 0.8em;cursor:pointer;border-bottom:1px solid #f5f5f5;font-size:0.9em;transition:background 0.1s;';
      item.innerHTML = `<strong>${city.label}</strong><span style="color:#737373;margin-left:0.5em;">${city.country}</span>`;
      item.onmouseenter = () => {
        selectedIndex = index;
        updateSelection();
      };
      item.onclick = () => selectCity(city);
      resultsList.appendChild(item);
    });
    
    resultsList.style.display = 'block';
  });
  
  container.appendChild(searchInput);
  container.appendChild(resultsList);
  container.appendChild(btnContainer);
  
  document.getElementById('tz-results').insertAdjacentElement('beforebegin', container);
  searchInput.focus();
}

function removeZone(index) {
  targetZones.splice(index, 1);
  updateResults();
  autoUpdateBestTime();
}

function copyResults() {
  if (targetZones.length === 0) {
    alert('No collaborators added yet.');
    return;
  }
  
  const dateStr = document.getElementById('tz-date').value;
  const timeStr = document.getElementById('tz-time').value;
  const sourceTz = document.getElementById('tz-source').value;
  const sourceCity = worldCities.find(c => c.value === sourceTz);
  const sourceLabel = sourceCity ? `${sourceCity.label}, ${sourceCity.country}` : sourceTz;
  
  let text = `📅 Meeting Time\n`;
  text += `━━━━━━━━━━━━━━━━━━\n`;
  text += `${sourceLabel}: ${dateStr} ${timeStr}\n\n`;
  
  const sourceDate = new Date(`${dateStr}T${timeStr}:00`);
  
  targetZones.forEach(tz => {
    const cityInfo = worldCities.find(c => c.value === tz.value && c.label === tz.label);
    const tzLabel = cityInfo ? `${cityInfo.label}, ${cityInfo.country}` : tz.label;
    const formatter = new Intl.DateTimeFormat('en-US', {
      timeZone: tz.value,
      weekday: 'short',
      month: 'short',
      day: 'numeric',
      hour: '2-digit',
      minute: '2-digit',
      hour12: false
    });
    text += `${tzLabel}: ${formatter.format(sourceDate)}\n`;
  });
  
  navigator.clipboard.writeText(text).then(() => {
    const btn = document.querySelector('.tz-copy-btn');
    btn.textContent = '✓ Copied!';
    btn.classList.add('copied');
    setTimeout(() => {
      btn.textContent = '📋 Copy All Times';
      btn.classList.remove('copied');
    }, 2000);
  });
}

function downloadICS() {
  if (targetZones.length === 0) {
    alert('No collaborators added yet.');
    return;
  }
  
  const dateStr = document.getElementById('tz-date').value;
  const timeStr = document.getElementById('tz-time').value;
  const sourceTz = document.getElementById('tz-source').value;
  const sourceCity = worldCities.find(c => c.value === sourceTz);
  const sourceLabel = sourceCity ? sourceCity.label : 'Meeting';
  
  // Parse date and time
  const [year, month, day] = dateStr.split('-').map(Number);
  const [hour, minute] = timeStr.split(':').map(Number);
  
  // Create start date (local time based on source timezone)
  const startDate = new Date(`${dateStr}T${timeStr}:00`);
  
  // Default meeting duration: 1 hour
  const endDate = new Date(startDate.getTime() + 60 * 60 * 1000);
  
  // Format date for ICS (UTC format: YYYYMMDDTHHMMSSZ)
  const formatICSDate = (date) => {
    return date.toISOString().replace(/[-:]/g, '').replace(/\.\d{3}/, '');
  };
  
  // Format date for DTSTART with timezone
  const formatICSDateLocal = (date) => {
    const y = date.getFullYear();
    const m = String(date.getMonth() + 1).padStart(2, '0');
    const d = String(date.getDate()).padStart(2, '0');
    const h = String(date.getHours()).padStart(2, '0');
    const min = String(date.getMinutes()).padStart(2, '0');
    return `${y}${m}${d}T${h}${min}00`;
  };
  
  // Build description with all timezone info
  let description = 'Meeting times for all participants:\\n\\n';
  description += `${sourceLabel}: ${dateStr} ${timeStr}\\n`;
  
  targetZones.forEach(tz => {
    const cityInfo = worldCities.find(c => c.value === tz.value && c.label === tz.label);
    const tzLabel = cityInfo ? cityInfo.label : tz.label;
    const formatter = new Intl.DateTimeFormat('en-US', {
      timeZone: tz.value,
      weekday: 'short',
      month: 'short',
      day: 'numeric',
      hour: '2-digit',
      minute: '2-digit',
      hour12: false
    });
    description += `${tzLabel}: ${formatter.format(startDate)}\\n`;
  });
  
  // Build attendee list for description
  const attendeeLocations = targetZones.map(tz => {
    const cityInfo = worldCities.find(c => c.value === tz.value && c.label === tz.label);
    return cityInfo ? cityInfo.label : tz.label;
  }).join(', ');
  
  // Generate unique ID
  const uid = `meeting-${Date.now()}-${Math.random().toString(36).substr(2, 9)}@timezone-converter`;
  
  // Create ICS content
  const icsContent = [
    'BEGIN:VCALENDAR',
    'VERSION:2.0',
    'PRODID:-//Timezone Converter//guhaogao.com//EN',
    'CALSCALE:GREGORIAN',
    'METHOD:PUBLISH',
    'BEGIN:VEVENT',
    `UID:${uid}`,
    `DTSTAMP:${formatICSDate(new Date())}`,
    `DTSTART;TZID=${sourceTz}:${formatICSDateLocal(startDate)}`,
    `DTEND;TZID=${sourceTz}:${formatICSDateLocal(endDate)}`,
    `SUMMARY:Meeting (${sourceLabel} + ${attendeeLocations})`,
    `DESCRIPTION:${description}`,
    'STATUS:CONFIRMED',
    'END:VEVENT',
    'END:VCALENDAR'
  ].join('\r\n');
  
  // Create download link
  const blob = new Blob([icsContent], { type: 'text/calendar;charset=utf-8' });
  const url = URL.createObjectURL(blob);
  const link = document.createElement('a');
  link.href = url;
  link.download = `meeting-${dateStr}-${timeStr.replace(':', '')}.ics`;
  document.body.appendChild(link);
  link.click();
  document.body.removeChild(link);
  URL.revokeObjectURL(url);
  
  // Update button state
  const btn = document.getElementById('tz-ics-btn');
  btn.textContent = '✓ Downloaded!';
  btn.classList.add('downloaded');
  setTimeout(() => {
    btn.textContent = '📅 Download .ics';
    btn.classList.remove('downloaded');
  }, 2000);
}

// Calculate penalty score for a given hour (0-23)
// Lower score = better time
function getTimePenalty(hourInMinutes) {
  const hour = hourInMinutes / 60;
  
  // Midnight to 6am: Heavy penalty (sleep time)
  if (hour >= 0 && hour < 6) {
    return 100 + (6 - hour) * 20; // 100-220 penalty
  }
  // 6am to 8am: Moderate penalty (early morning)
  if (hour >= 6 && hour < 8) {
    return 30 + (8 - hour) * 15; // 30-60 penalty
  }
  // 8am to 9am: Light penalty
  if (hour >= 8 && hour < 9) {
    return 10;
  }
  // 9am to 18pm: Ideal working hours - no penalty
  if (hour >= 9 && hour < 18) {
    return 0;
  }
  // 18pm to 20pm: Light penalty (evening)
  if (hour >= 18 && hour < 20) {
    return 10 + (hour - 18) * 5; // 10-20 penalty
  }
  // 20pm to 22pm: Moderate penalty
  if (hour >= 20 && hour < 22) {
    return 30 + (hour - 20) * 15; // 30-60 penalty
  }
  // 22pm to midnight: Heavy penalty
  if (hour >= 22) {
    return 80 + (hour - 22) * 10; // 80-100 penalty
  }
  return 50; // fallback
}

// Calculate distance from ideal working hours center (13:30 = 810 minutes)
function getWorkingHoursDistance(timeInMinutes, workStart, workEnd) {
  const workCenter = (workStart + workEnd) / 2;
  const workHalfRange = (workEnd - workStart) / 2;
  
  // If within working hours, calculate distance from center
  if (timeInMinutes >= workStart && timeInMinutes <= workEnd) {
    return Math.abs(timeInMinutes - workCenter) / workHalfRange * 10; // 0-10 score
  }
  
  // If outside working hours, add extra penalty based on distance
  if (timeInMinutes < workStart) {
    return 20 + (workStart - timeInMinutes) / 30; // 20+ penalty
  }
  return 20 + (timeInMinutes - workEnd) / 30; // 20+ penalty
}

function suggestBestTime() {
  if (targetZones.length === 0) {
    document.getElementById('tz-suggestion-result').innerHTML = '';
    return;
  }
  
  const dateStr = document.getElementById('tz-date').value;
  const sourceTz = document.getElementById('tz-source').value;
  const workStartStr = document.getElementById('tz-work-start').value;
  const workEndStr = document.getElementById('tz-work-end').value;
  const prioritySelect = document.getElementById('tz-priority');
  const focusTzValue = prioritySelect.value;
  const hasFocusCity = focusTzValue !== 'none';
  const focusTz = hasFocusCity ? focusTzValue : sourceTz; // Use source for AM/PM split when no focus
  const forceWorkHours = hasFocusCity && document.getElementById('tz-force-work').checked;
  
  const workStart = parseInt(workStartStr.split(':')[0]) * 60 + parseInt(workStartStr.split(':')[1]);
  const workEnd = parseInt(workEndStr.split(':')[0]) * 60 + parseInt(workEndStr.split(':')[1]);
  
  // All timezones to consider (source + targets)
  const allZones = [{ value: sourceTz, label: 'Your timezone' }, ...targetZones];
  
  // For "fair mode" (no priority), find two good but different options
  // For "priority mode", split by AM/PM of priority participant
  let bestOption1 = { hour: 10, score: Infinity, breakdown: [] };
  let bestOption2 = { hour: 14, score: Infinity, breakdown: [] };
  
  // Collect all scored slots first
  const allSlots = [];
  
  // Check every 30-minute slot
  for (let slot = 0; slot < 48; slot++) {
    const hour = Math.floor(slot / 2);
    const minute = (slot % 2) * 30;
    const testDate = new Date(`${dateStr}T${hour.toString().padStart(2, '0')}:${minute.toString().padStart(2, '0')}:00`);
    
    // Check focus city time first (only relevant when hasFocusCity)
    const focusTime = getTimeInZone(testDate, focusTz);
    
    // If force working hours is enabled, skip times outside working hours for focus city
    if (forceWorkHours) {
      if (focusTime < workStart || focusTime > workEnd) {
        continue; // Skip this slot
      }
    }
    
    let totalScore = 0;
    let breakdown = [];
    let hasExtremeTime = false;
    
    for (const tz of allZones) {
      const timeInMinutes = getTimeInZone(testDate, tz.value);
      const timePenalty = getTimePenalty(timeInMinutes);
      const distancePenalty = getWorkingHoursDistance(timeInMinutes, workStart, workEnd);
      const zoneScore = timePenalty + distancePenalty;
      
      // Check for extreme times (midnight to 6am)
      const hourInZone = timeInMinutes / 60;
      if (hourInZone >= 0 && hourInZone < 6) {
        hasExtremeTime = true;
      }
      
      totalScore += zoneScore;
      
      const cityInfo = worldCities.find(c => c.value === tz.value && c.label === tz.label);
      const label = cityInfo ? cityInfo.label : (tz.label === 'Your timezone' ? 'You' : tz.value);
      breakdown.push({
        label,
        value: tz.value,
        timeInMinutes,
        score: zoneScore,
        timePenalty,
        distancePenalty
      });
    }
    
    // Add extra penalty for having any extreme time
    if (hasExtremeTime) {
      totalScore += 50;
    }
    
    allSlots.push({ hour, minute, score: totalScore, breakdown: [...breakdown], focusTime });
  }
  
  if (hasFocusCity) {
    // Priority mode: split by AM/PM of priority participant
    for (const slot of allSlots) {
      const isAM = slot.focusTime < 720; // 720 = 12:00
      if (isAM && slot.score < bestOption1.score) {
        bestOption1 = slot;
      } else if (!isAM && slot.score < bestOption2.score) {
        bestOption2 = slot;
      }
    }
  } else {
    // Fair mode: find two good options with at least 3-hour difference
    // Sort by score to get best options
    allSlots.sort((a, b) => a.score - b.score);
    
    if (allSlots.length > 0) {
      bestOption1 = allSlots[0];
      
      // Find second best that's at least 3 hours different
      for (const slot of allSlots) {
        const hourDiff = Math.abs((slot.hour + slot.minute/60) - (bestOption1.hour + bestOption1.minute/60));
        if (hourDiff >= 3 && slot.score < bestOption2.score) {
          bestOption2 = slot;
          break;
        }
      }
      
      // If no option with 3+ hour difference, just take second best
      if (bestOption2.score === Infinity && allSlots.length > 1) {
        bestOption2 = allSlots[1];
      }
    }
  }
  
  // Get focus city label for display
  const focusCityInfo = hasFocusCity ? getFocusCityInfo(focusTz) : null;
  
  // Collect more alternatives (different from main options, at least 2 hours apart)
  const moreOptions = [];
  const usedHours = new Set();
  usedHours.add(bestOption1.hour);
  usedHours.add(bestOption2.hour);
  
  // Sort all slots by score
  const sortedSlots = [...allSlots].sort((a, b) => a.score - b.score);
  
  for (const slot of sortedSlots) {
    if (moreOptions.length >= 4) break; // Max 4 more options
    if (slot.score === Infinity) continue;
    
    // Check if this slot is at least 2 hours away from all used hours
    let tooClose = false;
    for (const usedHour of usedHours) {
      const hourDiff = Math.abs((slot.hour + slot.minute/60) - usedHour);
      if (hourDiff < 2) {
        tooClose = true;
        break;
      }
    }
    
    if (!tooClose) {
      moreOptions.push(slot);
      usedHours.add(slot.hour + slot.minute/60);
    }
  }
  
  // Display both results with more options
  displaySuggestions(bestOption1, bestOption2, dateStr, sourceTz, workStart, workEnd, focusCityInfo, forceWorkHours, hasFocusCity, moreOptions);
}

function getFocusCityInfo(focusTz) {
  const sourceTz = document.getElementById('tz-source').value;
  if (focusTz === sourceTz) {
    const sourceCity = worldCities.find(c => c.value === sourceTz);
    return sourceCity ? `${sourceCity.label} (You)` : 'Your timezone';
  }
  const targetCity = targetZones.find(t => t.value === focusTz);
  if (targetCity) {
    const cityInfo = worldCities.find(c => c.value === targetCity.value && c.label === targetCity.label);
    return cityInfo ? cityInfo.label : targetCity.label;
  }
  return focusTz;
}

function updatePrioritySelector() {
  const select = document.getElementById('tz-priority');
  const sourceTz = document.getElementById('tz-source').value;
  const currentValue = select.value;
  
  // Build options - keep "Everyone equally" as first option
  select.innerHTML = '<option value="none">⚖️ Everyone equally</option>';
  
  // Add source (your) timezone
  const sourceCity = worldCities.find(c => c.value === sourceTz);
  const sourceOption = document.createElement('option');
  sourceOption.value = sourceTz;
  sourceOption.textContent = sourceCity ? `🏠 ${sourceCity.label} (You)` : '🏠 Your timezone';
  select.appendChild(sourceOption);
  
  // Add collaborator timezones
  targetZones.forEach(tz => {
    const cityInfo = worldCities.find(c => c.value === tz.value && c.label === tz.label);
    const option = document.createElement('option');
    option.value = tz.value;
    option.textContent = cityInfo ? `👤 ${cityInfo.label}, ${cityInfo.country}` : `👤 ${tz.label}`;
    option.dataset.label = tz.label;
    select.appendChild(option);
  });
  
  // Restore previous selection if still valid
  const validValues = ['none', sourceTz, ...targetZones.map(t => t.value)];
  if (currentValue && validValues.includes(currentValue)) {
    select.value = currentValue;
  }
  
  // Hide/show force work hours checkbox based on priority selection
  updateForceWorkVisibility();
}

function updateForceWorkVisibility() {
  const focusValue = document.getElementById('tz-priority').value;
  const forceWorkLabel = document.getElementById('tz-force-work-label');
  
  if (focusValue === 'none') {
    forceWorkLabel.style.display = 'none';
  } else {
    forceWorkLabel.style.display = 'flex';
  }
}

function displaySuggestions(bestAM, bestPM, dateStr, sourceTz, workStart, workEnd, focusCityLabel, forceWorkHours, hasFocusCity, moreOptions = []) {
  const resultDiv = document.getElementById('tz-suggestion-result');
  const sourceCity = worldCities.find(c => c.value === sourceTz);
  const sourceLabel = sourceCity ? sourceCity.label : sourceTz;
  
  const constraintInfo = (hasFocusCity && forceWorkHours)
    ? `<span style="color:#14532d;font-size:0.85em;">✓ ${focusCityLabel} constrained to working hours</span>` 
    : '';
  
  // Format quality emoji based on score
  const getQualityEmoji = (score, breakdownLength) => {
    const avgScore = score / breakdownLength;
    if (avgScore < 15) return '🌟';
    if (avgScore < 30) return '👍';
    if (avgScore < 50) return '👌';
    if (avgScore < 80) return '⚠️';
    return '😓';
  };
  
  // Format more options as compact list
  const formatMoreOptions = () => {
    if (moreOptions.length === 0) return '';
    
    const optionsHtml = moreOptions.map(opt => {
      const timeStr = `${opt.hour.toString().padStart(2, '0')}:${(opt.minute || 0).toString().padStart(2, '0')}`;
      const emoji = getQualityEmoji(opt.score, opt.breakdown.length);
      // Build tooltip with all times
      const tooltip = opt.breakdown.map(b => {
        const h = Math.floor(b.timeInMinutes / 60);
        const m = b.timeInMinutes % 60;
        return `${b.label}: ${h.toString().padStart(2, '0')}:${m.toString().padStart(2, '0')}`;
      }).join('\n');
      
      return `<div class="tz-mini-option" onclick="applyBestTime(${opt.hour}, ${opt.minute || 0}, this)" title="${tooltip}">
        <span class="tz-mini-option-quality">${emoji}</span>
        <span class="tz-mini-option-time">${timeStr}</span>
      </div>`;
    }).join('');
    
    return `
      <div class="tz-more-options">
        <div class="tz-more-options-title">📌 More alternatives for your time (hover for details):</div>
        <div class="tz-more-options-list">${optionsHtml}</div>
      </div>
    `;
  };
  
  const formatOption = (best, label) => {
    if (best.score === Infinity) {
      return `<div class="tz-suggestion-option disabled">
        <div class="tz-suggestion-option-title">${label}</div>
        <div style="color:#737373;font-size:0.9em;">No suitable time found</div>
      </div>`;
    }
    
    const timeStr = `${best.hour.toString().padStart(2, '0')}:${(best.minute || 0).toString().padStart(2, '0')}`;
    
    // Quality assessment
    const avgScore = best.score / best.breakdown.length;
    let quality, qualityEmoji, qualityClass;
    if (avgScore < 15) {
      quality = 'Excellent'; qualityEmoji = '🌟'; qualityClass = 'excellent';
    } else if (avgScore < 30) {
      quality = 'Good'; qualityEmoji = '👍'; qualityClass = 'good';
    } else if (avgScore < 50) {
      quality = 'Acceptable'; qualityEmoji = '👌'; qualityClass = 'acceptable';
    } else if (avgScore < 80) {
      quality = 'Challenging'; qualityEmoji = '⚠️'; qualityClass = 'challenging';
    } else {
      quality = 'Difficult'; qualityEmoji = '😓'; qualityClass = 'difficult';
    }
    
    let breakdownHtml = best.breakdown.map(b => {
      const hour = Math.floor(b.timeInMinutes / 60);
      const minute = b.timeInMinutes % 60;
      const tStr = `${hour.toString().padStart(2, '0')}:${minute.toString().padStart(2, '0')}`;
      const isInWorkHours = b.timeInMinutes >= workStart && b.timeInMinutes <= workEnd;
      const emoji = isInWorkHours ? '✓' : (hour >= 0 && hour < 7 ? '🌙' : (hour >= 20 ? '🌆' : '○'));
      return `<div>${emoji} <strong>${b.label}</strong>: ${tStr}</div>`;
    }).join('');
    
    return `
      <div class="tz-suggestion-option ${qualityClass}">
        <div class="tz-suggestion-option-header">
          <div class="tz-suggestion-option-title">${label}</div>
          <span class="tz-suggestion-score">${qualityEmoji} ${quality}</span>
        </div>
        <div class="tz-suggestion-time">${sourceLabel}: ${timeStr}</div>
        <div class="tz-suggestion-breakdown">${breakdownHtml}</div>
        <button class="tz-apply-btn" onclick="applyBestTime(${best.hour}, ${best.minute || 0}, this)">
          ✓ Apply This Time
        </button>
      </div>
    `;
  };
  
  // Different display based on whether there's a focus city
  if (hasFocusCity) {
    resultDiv.innerHTML = `
      <div class="tz-suggestion-result">
        <div class="tz-suggestion-title">🎯 Best Meeting Times Found</div>
        <div class="tz-suggestion-detail">
          Two options based on <strong>${focusCityLabel}</strong>'s morning/afternoon. ${constraintInfo}
        </div>
        <div class="tz-suggestion-options">
          ${formatOption(bestAM, `☀️ Morning in ${focusCityLabel}`)}
          ${formatOption(bestPM, `🌤️ Afternoon in ${focusCityLabel}`)}
        </div>
        ${formatMoreOptions()}
      </div>
    `;
  } else {
    // Fair mode: show two best options (at least 3 hours apart)
    resultDiv.innerHTML = `
      <div class="tz-suggestion-result">
        <div class="tz-suggestion-title">🎯 Best Meeting Times Found</div>
        <div class="tz-suggestion-detail">
          <span style="color:#14532d;">⚖️ Fair for everyone</span> — two options optimized to minimize inconvenience for all participants.
        </div>
        <div class="tz-suggestion-options">
          ${formatOption(bestAM, `🥇 Best Option`)}
          ${formatOption(bestPM, `🥈 Alternative`)}
        </div>
        ${formatMoreOptions()}
      </div>
    `;
  }
}

function applyBestTime(hour, minute, buttonElement) {
  document.getElementById('tz-time').value = `${hour.toString().padStart(2, '0')}:${(minute || 0).toString().padStart(2, '0')}`;
  updateResults();
  
  // Reset all apply buttons to default state
  document.querySelectorAll('.tz-apply-btn').forEach(btn => {
    btn.classList.remove('applied');
    btn.innerHTML = '✓ Apply This Time';
    btn.disabled = false;
  });
  
  // Mark clicked button as applied
  if (buttonElement) {
    buttonElement.classList.add('applied');
    buttonElement.innerHTML = '✓ Applied';
  }
  
  // Scroll to results
  document.getElementById('tz-results').scrollIntoView({ behavior: 'smooth', block: 'start' });
}

// Initialize
document.addEventListener('DOMContentLoaded', init);
if (document.readyState !== 'loading') init();
</script>

## Features

- **Auto-detect timezone**: Automatically detects your local timezone based on browser settings
- **100+ world cities**: Search from major cities across all continents, including university towns (Cambridge, Stanford, Oxford, etc.)
- **Keyboard navigation**: Use ↑↓ arrows to navigate search results, Enter to select, Esc to cancel
- **Working hours indicator**: Visual markers show which times fall within/outside working hours
- **Overlap detection**: Highlights when all participants are in their working hours simultaneously
- **🎯 Smart Best Time Finder**:
  - **Priority mode**: Optimize around a specific participant's schedule (AM/PM options)
  - **Fair mode**: Find times that minimize inconvenience for everyone equally
  - **Smart scoring**: Heavily penalizes sleep hours (0-6am), moderately penalizes early/late hours
  - **Multiple alternatives**: Shows additional backup time options at a glance
- **📋 Copy all times**: One-click copy of formatted meeting times for easy sharing
- **📅 ICS download**: Export to calendar file compatible with Google Calendar, Apple Calendar, Outlook, etc.

## Tips for Scheduling International Meetings

| Route | Recommended Time | Notes |
|-------|-----------------|-------|
| **Asia ↔ Europe** | 08:00-10:00 HKT | Afternoon in Europe (15:00-17:00 CET) |
| **Asia ↔ US East** | 21:00-22:00 HKT | Morning in NYC (08:00-09:00 EST) |
| **Asia ↔ US West** | 09:00-10:00 HKT | Evening before in SF (17:00-18:00 PST, previous day) |
| **Europe ↔ US East** | 14:00-17:00 GMT | Morning in US (09:00-12:00 EST) |
| **Australia ↔ Europe** | 08:00-09:00 AEDT | Evening before in Europe (21:00-22:00 CET) |

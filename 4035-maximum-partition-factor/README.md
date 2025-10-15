<h2><a href="https://leetcode.com/problems/maximum-partition-factor">Maximum Partition Factor</a></h2> <img src='https://img.shields.io/badge/Difficulty-Hard-red' alt='Difficulty: Hard' /><hr><p>You are given a 2D integer array <code>points</code>, where <code>points[i] = [x<sub>i</sub>, y<sub>i</sub>]</code> represents the coordinates of the <code><font>i<sup>th</sup></font></code> point on the Cartesian plane.</p>

<p>The <strong>Manhattan distance</strong> between two points <code>points[i] = [x<sub>i</sub>, y<sub>i</sub>]</code> and <code>points[j] = [x<sub>j</sub>, y<sub>j</sub>]</code> is <code>|x<sub>i</sub> - x<sub>j</sub>| + |y<sub>i</sub> - y<sub>j</sub>|</code>.</p>

<p>Split the <code>n</code> points into <strong>exactly two non-empty</strong> groups. The <strong>partition factor</strong> of a split is the <strong>minimum</strong> Manhattan distance among all unordered pairs of points that lie in the same group.</p>

<p>Return the <strong>maximum</strong> possible <strong>partition factor</strong> over all valid splits.</p>

<p>Note: A group of size 1 contributes no intra-group pairs. When <code>n = 2</code> (both groups size 1), there are no intra-group pairs, so define the partition factor as 0.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span>points = [[0,0],[0,2],[2,0],[2,2]]</span></p>

<p><strong>Output:</strong> <span>4</span></p>

<p><strong>Explanation:</strong></p>

<p>We split the points into two groups: <code>{[0, 0], [2, 2]}</code> and <code>{[0, 2], [2, 0]}</code>.</p>

<ul>
	<li>
	<p>In the first group, the only pair has Manhattan distance <code>|0 - 2| + |0 - 2| = 4</code>.</p>
	</li>
	<li>
	<p>In the second group, the only pair also has Manhattan distance <code>|0 - 2| + |2 - 0| = 4</code>.</p>
	</li>
</ul>

<p>The partition factor of this split is <code>min(4, 4) = 4</code>, which is maximal.</p>
</div>

<p><strong>Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span>points = [[0,0],[0,1],[10,0]]</span></p>

<p><strong>Output:</strong> <span>11</span></p>

<p><strong>Explanation:​​​​​​​</strong></p>

<p>We split the points into two groups: <code>{[0, 1], [10, 0]}</code> and <code>{[0, 0]}</code>.</p>

<ul>
	<li>
	<p>In the first group, the only pair has Manhattan distance <code>|0 - 10| + |1 - 0| = 11</code>.</p>
	</li>
	<li>
	<p>The second group is a singleton, so it contributes no pairs.</p>
	</li>
</ul>

<p>The partition factor of this split is <code>11</code>, which is maximal.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= points.length &lt;= 500</code></li>
	<li><code>points[i] = [x<sub>i</sub>, y<sub>i</sub>]</code></li>
	<li><code>-10<sup>8</sup> &lt;= x<sub>i</sub>, y<sub>i</sub> &lt;= 10<sup>8</sup></code></li>
</ul>

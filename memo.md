1. Creational（生成に関するパターン）
Singleton
インスタンスが1つしか存在しないことを保証するパターン。

Factory Method
オブジェクトの生成をサブクラスに委譲するパターン。

Abstract Factory
関連するオブジェクト群を生成するためのインターフェースを提供するパターン。

Builder
複雑なオブジェクトを段階的に構築するパターン。

Prototype
既存のオブジェクトをコピーして新しいインスタンスを生成するパターン。

2. Structural（構造に関するパターン）
Adapter
既存のクラスに別のインターフェースを与えるパターン。

Bridge
抽象と実装を分離し、それぞれ独立して変更できるようにするパターン。

Composite
オブジェクトをツリー構造にして、個別のオブジェクトとグループを同一視できるようにするパターン。

Decorator
オブジェクトに動的に機能を追加するパターン。

Facade
サブシステムへのシンプルなインターフェースを提供するパターン。

Flyweight
オブジェクトを共有し、メモリを効率的に使うパターン。

Proxy
他のオブジェクトへのアクセスを制御するパターン。

3. Behavioral（振る舞いに関するパターン）
Chain of Responsibility
リクエストを処理できるオブジェクトが複数ある場合、処理の責任を持つオブジェクトを決定するパターン。

Command
要求をオブジェクトとしてカプセル化し、処理を遅延させたりログに記録できるパターン。

Interpreter
言語の文法を表現し、式を評価するパターン。

Iterator
コレクション内の要素に順にアクセスするためのインターフェースを提供するパターン。

Mediator
オブジェクト間のやりとりを調整するパターン。

Memento
オブジェクトの状態を保存し、後でその状態に戻すパターン。

Observer
オブジェクトの状態が変化した際に、依存している他のオブジェクトに通知するパターン。

State
オブジェクトの内部状態に応じて、振る舞いを変えるパターン。

Strategy
振る舞いをカプセル化し、実行時に切り替えられるようにするパターン。

Template Method
処理の枠組みを定義し、具体的な処理をサブクラスに委譲するパターン。

Visitor
オブジェクトの構造に新しい操作を定義できるパターン。

4. その他のパターン
Dependency Injection
オブジェクトの依存関係を外部から注入するパターン。テストや保守性の向上に有効です。

MVC（Model-View-Controller）
アプリケーションをモデル、ビュー、コントローラーの3つの責務に分けるアーキテクチャパターン。

5. そのほか
Repository Pattern
Specification Pattern
Event Sourcing Pattern
CQRS (Command Query Responsibility Segregation) Pattern
Unit Of Work Pattern
Observer Pattern in Reactive Programming (Reactive Observer)
Service Locator Pattern
Business Delegate Pattern
Data Access Object (DAO) Pattern。
Null Object Pattern
Event Aggregator Pattern
Specification Pattern
Active Object Pattern
Blackboard Pattern
Interpreter Pattern (再考)
Role Object Pattern
Model-View-ViewModel (MVVM) Pattern
Unit of Work Pattern
Retry Pattern
Scheduler Pattern
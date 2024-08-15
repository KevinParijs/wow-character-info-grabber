class Item:
    def __init__(self, data):
        self.item_id = data.get('item', {}).get('id', 0)
        self.name = data.get('name', '')
        self.item_class = data.get('item_class', {}).get('name', '')
        self.item_subclass = data.get('item_subclass', {}).get('name', '')
        self.level = data.get('level', {}).get('value', 0)
        self.quality = data.get('quality', {}).get('name', '')
        self.quantity = data.get('quantity', 0)
        self.modified_appearance_id = data.get('modified_appearance_id', 0)
        self.transmog_id = data.get('transmog', {}).get('item', {}).get('id', 0)
        self.stats = self.parse_stats(data.get('stats', []))
        self.enchantments = self.parse_enchantments(data.get('enchantments', []))
        self.sockets = self.parse_sockets(data.get('sockets', []))
        self.set_info = self.parse_set(data.get('set', {}))

    def parse_stats(self, stats):
        return [{'type': stat['type']['name'], 'value': stat['value']} for stat in stats]

    def parse_enchantments(self, enchantments):
        return [{'display_string': enchantment['display_string'],
                 'source_item_id': enchantment.get('source_item', {}).get('id', 0)} for enchantment in enchantments]

    def parse_sockets(self, sockets):
        return [{'type': socket['socket_type']['name'],
                 'socket_item_id': socket.get('item', {}).get('id', 0)} for socket in sockets]

    def parse_set(self, item_set):
        return {
            'name': item_set.get('item_set', {}).get('name', ''),
            'effects': item_set.get('display_string', '')
        }

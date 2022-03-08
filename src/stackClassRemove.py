      def remove(self, index):
          before = None
          current = self.head.next
          for _index in range(self.count):
              if _index == index:
                  if _index == 0:
                      self.head.next = current.next
                  else:
                      before.next = current.next

              before = current
              current = current.next
          self.count -= 1
